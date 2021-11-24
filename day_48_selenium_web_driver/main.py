"""
    This script is doing some game playing with selenium
"""
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# reading our file that has a path to our chrome_driver_path
# started adding ability to get required info straight from user

try:
    file = open('../secret.json')
    secret_info = json.load(file)
    file.close()
    chrome_driver_path = secret_info['chrome_driver_path']
except FileNotFoundError:
    chrome_driver_path = input("Please Input the path of the chrome driver ").strip()

# driving the chrome browser and doing all of our automated task
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open a new web page at url
url = "https://www.python.org/"
driver.get(url=url)

events = driver.find_element(By.CLASS_NAME, "event-widget")
events_list = events.find_elements(By.TAG_NAME, 'li')
events_list_dic = []

for event in events_list:
    curr_event = event.text.split('\n')
    events_list_dic.append({"date": curr_event[0], "name": curr_event[1]})

print(events_list_dic)
