import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from git import Repo
from dotenv import load_dotenv
import time
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

service = FirefoxService(executable_path='/path/to/geckodriver')
options = FirefoxOptions()

driver = Firefox(service=service, options=options)

load_dotenv()

# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

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
driver.get(os.getenv("URL"))
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

level = driver.find_element(
    By.XPATH, "//div[@class='small-hex is-extra-wide is-inline mr-15px is-white-rank']")
folder_kata = level.text

code_element = driver.find_element(
    By.XPATH, "//div[@class='items-list w-full md:w-2/3 md:pl-4 md:border-l md:grow']")
code = code_element.text
# print(code)
driver.quit()

functions = re.findall(r"(\d+) kyu.*?Python:(.*?)(?=\n\d|\Z)", code, re.DOTALL)


def build_functions(func_list):
    functions = {}
    repo_dir = "D:\job\Codewwars\codewars"
    repo = Repo.init(repo_dir)
    for func in func_list:
        kyu = func[0]
        func_code = func[1].replace(
            "\nlast month\nRefactor\nDiscuss", "").split("Refactor")[0]
        func_name = re.search(r'def (\w+)', func_code).group(1)
        folder_name = "kyu_" + kyu
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_name = os.path.join(folder_name, func_name + ".py")
        with open(file_name, "w") as f:
            f.write(func_code.replace("last month", ""))
        functions[func_name] = file_name
        if os.path.exists(os.path.join(folder_name, file_name)):
            repo.git.add(os.path.join(folder_name, file_name))
            repo.index.commit("Update file_name")
        else:
            repo.git.add(A=True)
            repo.index.commit(f"Add kyu_{kyu} files")
    origin = repo.remote(name='origin')
    origin.push()
    return functions


build_functions(functions)
