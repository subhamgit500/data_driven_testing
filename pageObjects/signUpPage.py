import time

from faker import Faker
import random
import os
import secrets
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Sign_up_Page:

    name = (By.NAME,"name")
    email = (By.XPATH,"//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH,"//button[text()='Signup']")

    def __init__(self,driver):
        self.driver = driver


    def perform_signup(self):

        fake = Faker()
        name = fake.name()
        domain_list = ["gmail.com","yahoo.com","example.com"]
        email = f"{name.lower().replace(' ','')}{random.randint(100,999)}@{random.choice(domain_list)}"

        print("Name:",name)
        print("Email:",email)

        password_length = 10

        character = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(secrets.choice(character) for _ in range(password_length))
        print("Password:",password)

        folder_path = "C:\\Users\\subha\\Documents\\User Data"
        os.makedirs(folder_path,exist_ok = True)
        file_path = os.path.join(folder_path,"users.txt")
        with open(file_path,"a") as f:
            f.write(f"Name : {name} \nEmail: {email} \nPassword: {password} \n{'-'*50} \n")


        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        time.sleep(1)
        self.driver.find_element(*self.signup_btn).click()
        time.sleep(1)

        #To select gender
        self.driver.find_element(By.ID,"id_gender1").click()
        time.sleep(1)
        #To enter password
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,300);")
        #To DOB


        #To enter first name
        name_arr = name.split(" ")
        self.driver.find_element(By.ID,"first_name").send_keys(name_arr[0])
        time.sleep(1)
        self.driver.find_element(By.ID,"last_name").send_keys(name_arr[1])

        self.driver.find_element(By.CSS_SELECTOR,"#address1").send_keys("Pune, India")

        self.driver.execute_script("window.scrollBy(0,100);")

        #To select country
        country = Select(self.driver.find_element(By.ID,"country"))
        country.select_by_value("India")

        # To select state
        self.driver.find_element(By.CSS_SELECTOR,"#state").send_keys("Maharastra")
        # To select City
        self.driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Pune")
        # To select zipcode
        self.driver.find_element(By.CSS_SELECTOR, "#zipcode").send_keys("1254454")
        # To select mobile_number
        self.driver.find_element(By.CSS_SELECTOR, "#mobile_number").send_keys("655658575")

        time.sleep(1)
        # To click on create account
        self.driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()
        time.sleep(3)


