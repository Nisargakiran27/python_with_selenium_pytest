from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

class CartPage:
    """
    This page is all about the cart.
    We keep locators for items in the cart and the checkout button here.
    """
    def __init__(self,driver):
        """
        Keep the driver and load all cart-related locators from .env.
        """
        self.driver = driver
        self.cart_item = (By.CLASS_NAME,os.getenv("CART_ITEM"))
        self.checkout = (By.ID,os.getenv("CART_CHECKOUT_BUTTON"))


    def get_cart_item(self):
        """
        Get all the products currently in the cart.
        """
        return self.driver.find_elements(*self.cart_item)
    
    def click_checkout(self):
        """
        Click the checkout button to move to the next step.
        """
        self.driver.find_element(*self.checkout).click()

    