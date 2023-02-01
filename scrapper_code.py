import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from git import Repo
from dotenv import load_dotenv
import time
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.chrome.options import Options
import git

load_dotenv()
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)



# driver = webdriver.Chrome(executable_path='/path/to/chromedriver', desired_capabilities=chrome_options.to_capabilities())

driver.get("https://www.codewars.com/users/sign_in")

driver.implicitly_wait(10)

username_field = driver.find_element(By.ID, "user_email")

username_field.send_keys(os.getenv("USER_EMAIL"))

password_field = driver.find_element(By.ID, "user_password")

password_field.send_keys(os.getenv("PASS"))

login_button = driver.find_element(By.XPATH,
                                   "//button[@class='btn mt-3 w-full text-center inline-flex items-center justify-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white dark:text-gray-200 is-red focus:outline-none focus:ring-2 focus:ring-blue-400 dark:focus:ring-cgray-600']")

login_button.click()

driver.implicitly_wait(10)
driver.get("https://www.codewars.com/users/joshua_abel27/completed_solutions")
last_height = driver.execute_script(
    "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script(
        "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    if new_height == last_height:
        break
    last_height = new_height

# level = driver.find_element(
#     By.XPATH, "//div[@class='small-hex is-extra-wide is-inline mr-15px is-white-rank']")
# folder_kata = level.text

code_element = driver.find_element(
    By.XPATH, "//div[@class='items-list w-full md:w-2/3 md:pl-4 md:border-l md:grow']")
code = code_element.text
# print(code)
driver.quit()

functions = re.findall(r"(\d+) kyu.*?Python:(.*?)(?=\n\d|\Z)", code, re.DOTALL)


def build_functions(func_list):
    functions = {}
    repo_dir = '.'
    repo = Repo.init(repo_dir)
    for func in func_list:
        kyu = func[0]
        func_code = func[1].replace("\nlast month\nRefactor\nDiscuss", "").split("Refactor")[0]
        func_name = re.search(r'def (\w+)', func_code).group(1)
        folder_name = "kyu_" + kyu
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_name = os.path.join(folder_name, func_name + ".py")
        with open(file_name, "w") as f:
            f.write(func_code.replace("last month", ""))
        functions[func_name] = file_name
        if os.path.exists(os.path.join(folder_name, file_name)):
            with open(".gitmodules", "a") as f:
              f.write(f"[submodule \"kyu_{kyu}\"]\n\tpath = kyu_6\n\turl = https://github.com/joshuaabel1/Codewars/tree/main/kyu_{kyu}\n")
            repo.git.add(os.path.join(folder_name, file_name))
            repo.index.commit(f"Update {file_name}")
        else:
            repo.git.add(A=True)
            repo.index.commit(f"Add kyu_{kyu} files")
    # Remove remote "origin" if it exists
    try:
        repo.remote("origin").remove(repo, "origin")
    except git.exc.GitCommandError as e:
        # Do nothing if remote "origin" doesn't exist
        pass
    repo.create_submodule(f"kyu_{kyu}", f"https://github.com/joshuaabel1/Codewars/tree/main/kyu_{kyu}")
    # Create new remote "origin"
    origin = repo.create_remote(name='origin', url='https://github.com/joshuaabel1/Codewars.git')
    try:
        origin.push(refspec="main")
    except git.exc.GitCommandError as e:
        print(e)

    repo.git.submodule("init")
    repo.git.submodule("update")

    return functions


build_functions(functions)
