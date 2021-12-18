"""
    Essentially it goes in an follows the followers of  the target account
    Project stopped, did not want to continue with project to not lock the account
    planning on creating new account if I want to continue later
"""
import json
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

EMAIL = ""
PASSWORD = ""
TARGET_ACCOUNT = ""


def configure_logger():
    """ configure the logger and the directory to log to"""
    if not os.path.isdir('logs'):
        os.mkdir('logs')

    ran_at = str(datetime.now().strftime('%Y-%m-%d_%I-%M-%S'))
    logging.basicConfig(filename=f'logs/{ran_at}.log', level=logging.DEBUG)
    logging.basicConfig()


def get_chrome_driver_path():
    """
        looks for the path of the chrome driver I downloaded in 'secret.json'
        which I am using sort like a config file. if the file does not exist
        asks the user to enter the path
    """
    try:
        file = open('../secret.json')
        secret_info = json.load(file)
        file.close()
        return secret_info['chrome_driver_path']
    except FileNotFoundError:
        return input("Please Input the path of the chrome driver ").strip()


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=get_chrome_driver_path())

    def login(self):
        """login to instagram with your credentials"""
        url = "https://www.instagram.com/accounts/login/"
        email = EMAIL if EMAIL != "" else input('enter email: ')
        password = PASSWORD if PASSWORD != "" else input("enter password: ")
        self.driver.get(url)

        time.sleep(2)  # this is just to get the browser time to load

        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(email)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        login_btn = self.driver.find_element(By.CLASS_NAME, "L3NKy")
        print(login_btn.text)
        login_btn.click()

    def find_followers(self):
        time.sleep(2)
        target = TARGET_ACCOUNT if TARGET_ACCOUNT != "" else input('enter target account: ')
        search_field = self.driver.find_element(By.CSS_SELECTOR, "XTCLo")
        search_field.send_keys(target)

    def follow(self):
        pass

    def run(self):
        self.login()
        self.find_followers()
        self.follow()


if __name__ == "__main__":
    bot = InstaFollower()
    bot.run()
