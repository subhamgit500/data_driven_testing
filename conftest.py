import time

import pytest
from selenium import webdriver

@pytest.fixture
def browserSetup():

    driver = webdriver.Chrome()

    driver.get("https://automationexercise.com/login")
    driver.maximize_window()
    driver.implicitly_wait(5)

    time.sleep(1)

    yield driver

    driver.quit()