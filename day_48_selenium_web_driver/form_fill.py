"""
    Using Selenium to fill out form
"""
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    file = open('../secret.json')
    secret_info = json.load(file)
    file.close()
    chrome_driver_path = secret_info['chrome_driver_path']
except FileNotFoundError:
    chrome_driver_path = input("Please Input the path of the chrome driver ").strip()




# Get user input
first_name_input = input("Enter First name: ")
last_name_input =  input("Enter Last name: ")
email_input =  input("Enter email address: ")

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

input('ready ?')
fname = driver.find_element(By.NAME, "fName")
fname.send_keys(first_name_input)

lname = driver.find_element(By.NAME, "lName")
lname.send_keys(last_name_input)

email = driver.find_element(By.NAME, "email")
email.send_keys(email_input)

button = driver.find_element(By.TAG_NAME,  "button")
button.click()

input("done ?")
driver.quit()
exit(0)




