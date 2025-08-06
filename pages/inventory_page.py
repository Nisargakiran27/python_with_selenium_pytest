# import random
# from selenium.webdriver.common.by import By

# class InventoryPage:
#     def __init__(self, driver):
#         self.driver = driver

#     def click_random_product(self):
#         products = self.driver.find_elements(By.XPATH,"//div[@class='inventory_item']")
#         random_product = random.choice(products)

#         product_link = random_product.find_element(By.CLASS_NAME,"inventory_item_name")
#         product_link.click()



import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.XPATH,"//div[@class='app_logo']")
        self.cart_icon = (By.XPATH,"//div[@class='shopping_cart_container']")
        self.dropdown = (By.XPATH,"//span[@class='active_option']")
        self.add_to_cart_btn = (By.XPATH,"//button[contains(@class, 'btn_primary') and text()='Add to cart']")
        self.cart_btn = (By.CLASS_NAME,"shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME,"shopping_cart_badge")

    def click_random_product(self):
        products = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item']")
        random_product = random.choice(products)
        product_link = random_product.find_element(By.CLASS_NAME, "inventory_item_name")
        product_link.click()

    # def click_add_to_cart(self):
    #     self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn_primary') and text()='Add to cart']").click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def click_cart_icon(self):
        # self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(*self.cart_btn).click()

    def check_logo(self):
        return self.driver.find_element(*self.logo).is_displayed()
    
    def check_cart_icon(self):
        return self.driver.find_element(*self.cart_icon).is_displayed()
    
    def cart_badge_check(self):
        wait = WebDriverWait(self.driver , 10)
        return wait.until(EC.visibility_of_element_located(self.cart_badge)).is_displayed()


    def badge_count(self):
        return self.driver.find_element(*self.cart_badge).text