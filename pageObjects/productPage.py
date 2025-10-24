import time

from selenium.webdriver.common.by import By


class ProductPage:

    product_btn = (By.XPATH, "//a[@href='/products']")
    search_box = (By.ID,"search_product")
    search_btn = (By.ID,"submit_search")
    view_product_btn = (By.XPATH,"//a[@href='/product_details/1']")

    def __init__(self,driver):
        self.driver = driver

    def search_product(self,product_to_search):

        self.driver.find_element(*self.product_btn).click()
        time.sleep(2)
        self.driver.find_element(*self.search_box).send_keys(product_to_search)
        time.sleep(1)
        self.driver.find_element(*self.search_btn).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,400);")
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,0);")
        print(f"{product_to_search} entered in search box.")


    def verify_product_page(self):

        self.driver.find_element(*self.product_btn).click()  #clicking on product tab
        time.sleep(2)

        #verifying product page
        all_product = self.driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
        assert all_product == "ALL PRODUCTS"
        print("You are in product page")

        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0,600);")
        time.sleep(1)

        self.driver.find_element(*self.view_product_btn).click()

        #verifying product name
        product_name = self.driver.find_element(By.XPATH,"//div[@class='product-information']/h2").text
        assert product_name == "Blue Top"
        print("Successfully verified product name.")
        time.sleep(2)
        #verifying product price
        product_price = self.driver.find_element(By.XPATH,"//div[@class='product-information']/span/span").text
        assert "500" in product_price
        print("Successfully verified product price.")

        #verifying product brand
        product_brand = self.driver.find_element(By.XPATH,"//div[@class='product-information']/p[4]").text
        assert "Polo" in product_brand
        print("Successfully verified product brand.")


