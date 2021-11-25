"""
    The goal of today's project is to learn to use Selenium to automate applying for jobs posted on Linkedin
    The program uses LinkedIn's "Easy Apply" function to send applications to all the jobs
    that meet your criteria (instead of just a single listing).

    ***
        This program also does not do application that requires user to fill out form and
        currently it does not click on the 'Submit application' button but rather prints out
        'Submit application' because I did not want to needlessly apply to job applications
    ***
"""

import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import logging
from datetime import datetime
import os

if not os.path.isdir('logs'):
    os.mkdir('logs')

ran_at = str(datetime.now().strftime('%Y-%m-%d_%I-%M-%S'))
logging.basicConfig(filename=f'logs/{ran_at}.log', level=logging.DEBUG)
logging.basicConfig()

try:
    file = open('../secret.json')
    secret_info = json.load(file)
    file.close()
    chrome_driver_path = secret_info['chrome_driver_path']
except FileNotFoundError:
    chrome_driver_path = input("Please Input the path of the chrome driver ").strip()

# you can set email at the beginning of the script or you can wait for program to prompt for it
email = ""
password = ""

if email == "":
    email = input('enter email or phone_number: ')
if password == "":
    password = input('enter password: ')


class JobGetter:
    url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102380872&keywords=python%20developer&location=Boston%2C%20Massachusetts%2C%20United%20States"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def run(self):
        # opens the browser at the specified url
        self.driver.get(url=JobGetter.url)
        self.sign_in()
        # todo automate
        # I did this because I haven't found how to make only a section of the page scroll down
        # input('scroll through the job section to make it loaded, then press enter')
        self.apply_to_jobs()
        self.driver.quit()

    def apply_to_jobs(self):
        jobs = self.driver.find_elements(By.CLASS_NAME, 'job-card-container')
        logging.info(f'# of Jobs parsed: {len(jobs)}\n')
        print(f'# of Jobs parsed: {len(jobs)}\n')

        for current_job in jobs:
            current_job.click()
            self.driver.implicitly_wait(5)
            current_job_text = " | ".join(current_job.text.split('\n'))
            logging.info(f"JOB INFO: {current_job_text}\n")
            print(f"JOB INFO: {current_job_text}")

            # this 'time.sleep' was also used to give the browser time to load, although I don't like it
            # because the amount seconds was just chosen haphazardly, I suspect that there is a better solution
            # todo find better solution
            time.sleep(1)

            easy_apply_btn = self.driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
            easy_apply_btn.click()

            click_next = True
            while click_next:
                next_btn = self.driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
                if next_btn.text == "Next" or next_btn.text == "Review":
                    next_btn.click()
                    # try to catch errors, if
                    try:
                        errors = self.driver.find_element(By.CLASS_NAME, 'fb-form-element__error-text')
                        form_content = self.driver.find_element(By.CLASS_NAME,'jobs-easy-apply-modal__content').text
                        print('error found, quitting application, Moving to next job')
                        logging.warning('error found, quitting application, Moving to next job')
                        print(f"Error causing page content -> {form_content}")
                        logging.warning(f"Error causing page content -> {form_content}")
                        self.quit_application()
                        click_next = False
                    except NoSuchElementException:
                        pass
                    time.sleep(1)
                else:
                    if next_btn.text == "Submit application":
                        logging.info("Submit Application page reached")
                    else:
                        logging.warning("Unaccounted for Button")
                    self.quit_application()
                    click_next = False

    def quit_application(self):
        """ Quits the job application without submitting"""
        dismissed_btn = self.driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        dismissed_btn.click()
        time.sleep(1)
        modal_btns = self.driver.find_elements(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')
        for btn in modal_btns:
            if btn.text == "Discard":
                btn.click()

    def sign_in(self):
        """
        This method is used to get to the sign in page, provide the credential and attemp to login
        :return:
        """
        sign_in_btn = self.driver.find_element(By.CLASS_NAME, 'cta-modal__primary-btn')
        # this waits for the dom to load, otherwise it throws an error that the element is not interact able
        self.driver.implicitly_wait(5)
        sign_in_btn.click()
        # provide the sign in information and logs in automatically
        username_input = self.driver.find_element(By.ID, 'username')
        password_input = self.driver.find_element(By.ID, 'password')
        username_input.send_keys(email)
        password_input.send_keys(password)
        self.driver.find_element(By.CLASS_NAME, 'btn__primary--large').click()


if __name__ == '__main__':
    job_getter = JobGetter()
    job_getter.run()
