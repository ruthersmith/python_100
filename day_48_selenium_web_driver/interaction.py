"""
    This script uses selenium to interact with a wikipedia web page
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

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article_count_div = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count_div.text)
article_count_div.click()
driver.quit()