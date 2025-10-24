
import pytest
from pageObjects.loginPage import LoginPage
from utility.testdata import get_data_from_excel



test_data = get_data_from_excel("C:\\Users\\subha\\Documents\\test_data.xlsx")

@pytest.mark.parametrize("username,password,item",test_data)
def test_login(browserSetup,username,password,item):

    driver = browserSetup

    login_page = LoginPage(driver)
    login_page.perform_login(username,password)

    # product_page = login_page.go_to_product_page()
    # product_page.search_product(item)

    login_page.perform_logout()

@pytest.mark.parametrize("username,password,item",test_data)
def test_view_product(browserSetup,username,password,item):

    driver = browserSetup

    login_page = LoginPage(driver)
    login_page.perform_login(username,password)

    product_page = login_page.go_to_product_page()
    product_page.verify_product_page()

    login_page.perform_logout()


    #Testing GitHub
    #Testing GitHub from Pycharm

    #New changes has been done By person A











