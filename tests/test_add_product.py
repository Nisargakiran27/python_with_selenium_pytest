import pytest
from pages.login import LoginPages
from pages.inventory import InventoryPage
from pages.cart_page import CartPage
import time 
# from dotenv import load_dotenv
# import os 

# load_dotenv()
# username = os.getenv("USERNAME")
# password = os.getenv("PASSWORD")


def test_add_product_to_cart(setup):
    """
    Test Case: Add a random product to the cart and proceed to checkout.

    Steps:
    1. Open the SauceDemo website.
    2. Log in with valid credentials (standard_user / secret_sauce).
    3. Select a random product from the inventory.
    4. Add the selected product to the cart.
    5. Navigate to the cart page.
    6. Verify items in the cart and click checkout.

    Args:
        setup (fixture): Provides WebDriver instance and base URL.
    """
    driver, baseUrl = setup
    driver.get(baseUrl)

    login = LoginPages(driver)
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
