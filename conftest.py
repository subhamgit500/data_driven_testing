import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browserSetup():

    driver = webdriver.Chrome()

    driver.get("https://automationexercise.com/login")
    driver.maximize_window()
    driver.implicitly_wait(5)

    time.sleep(1)

    yield driver

    driver.quit()

