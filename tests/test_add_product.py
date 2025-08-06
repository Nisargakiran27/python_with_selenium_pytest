import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time 
# from dotenv import load_dotenv
# import os 

# load_dotenv()
# username = os.getenv("USERNAME")
# password = os.getenv("PASSWORD")


def test_add_product_to_cart(setup):
    driver, baseUrl = setup
    driver.get(baseUrl)

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    time.sleep(4)

    Inventory = InventoryPage(driver)
    Inventory.click_random_product()
    

    Inventory.click_add_to_cart()
    Inventory.click_cart_icon()
    time.sleep(4)

    cart = CartPage(driver)
    cart.get_cart_item()
    time.sleep(4)

    cart.click_checkout()
    time.sleep(4)
