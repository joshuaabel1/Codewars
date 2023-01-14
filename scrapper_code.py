import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from git import Repo
from dotenv import load_dotenv
load_dotenv()
driver = webdriver.Chrome()

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

# "//div[@class='items-list w-full md:w-2/3 md:pl-4 md:border-l md:grow']"
level = driver.find_element(By.XPATH, "//div[@class='small-hex is-extra-wide is-inline mr-15px is-white-rank']")
folder_kata = level.text

code_element = driver.find_element(By.XPATH, "//pre/code[@data-language='python']")
code = code_element.text

driver.quit()

if not os.path.exists(folder_kata):
    os.makedirs(folder_kata)


def create_function_file(code):
    lines = code.split("\n")
    function_name = re.search(r"def (\w+)\(", lines[0]).group(1)
    with open(f"{folder_kata}/{function_name}.py", "w") as f:
        f.write(code)
    print(f"El archivo {function_name}.py se ha guardado.")
    # git.add(f"{folder_kata}/{function_name}.py")
    repo_dir = 'D:\job\Codewwars\codewars'
    repo = Repo.init(repo_dir)
    repo.git.add(A=True)
    repo.index.commit(f"add {function_name}")
    origin = repo.remote(name='origin')
    origin.push()

create_function_file(code)



