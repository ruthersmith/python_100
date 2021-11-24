import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TIME_DELTA = 15
try:
    file = open('../secret.json')
    secret_info = json.load(file)
    file.close()
    chrome_driver_path = secret_info['chrome_driver_path']
except FileNotFoundError:
    chrome_driver_path = input("Please Input the path of the chrome driver ").strip()

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://orteil.dashnet.org/cookieclicker/")

timeout = time.time() + TIME_DELTA
while True:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()
    enabled_helpers = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
    if time.time() >= timeout:
        timeout = time.time() + TIME_DELTA
        if len(enabled_helpers) > 0:
            enabled_helpers[len(enabled_helpers) - 1].click()

