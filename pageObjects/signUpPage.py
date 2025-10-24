import time

from selenium.webdriver.common.by import By

class Sign_up_Page:

    name = (By.NAME,"name")
    email = (By.XPATH,"//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH,"//button[text()='Signup']")

    def __init__(self,driver):
        self.driver = driver


    def perform_signup(self):

        self.driver.find_element(*self.name).send_keys("Ana")
        self.driver.find_element(*self.email).send_keys("ana@gmail.com")
        time.sleep(2)
        self.driver.find_element(*self.signup_btn).click()
        time.sleep(2)