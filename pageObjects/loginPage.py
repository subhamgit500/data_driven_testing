import time

from selenium.webdriver.common.by import By

from pageObjects.productPage import ProductPage


class LoginPage:

    username_element = (By.NAME, "email")
    password_element = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[text()='Login']")
    logout_btn = (By.XPATH, "//a[@href='/logout']")
    def __init__(self,driver):
        self.driver = driver

    def perform_login(self,username,passwrod):

        self.driver.find_element(*self.username_element).send_keys(username)
        self.driver.find_element(*self.password_element).send_keys(passwrod)
        self.driver.find_element(*self.login_btn).click()

        print("Successfully clicked on Login button")

        time.sleep(2)

        logout_text = self.driver.find_element(By.XPATH, "//a[@href='/logout']").text
        assert "Logout" in logout_text, "Failed to verify login"  # 1st Validation

        logged_in_as_username = self.driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']/li[10]/a").text
        assert "John Cena" in logged_in_as_username, "Failed to verify login"  # 2nd Validation

        print("You are successfully logged in.")

    def perform_logout(self):

        self.driver.find_element(*self.logout_btn).click()
        time.sleep(2)

        login_text = self.driver.find_element(By.XPATH, "//div[@class='login-form']/h2").text
        assert "Login" in login_text
        print("You are successfully logged out.")

        self.driver.close()

    def go_to_product_page(self):
        return ProductPage(self.driver)


