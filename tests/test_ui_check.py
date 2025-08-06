import pytest
from selenium.webdriver.common.by import By
from utils.login import perform_login_and_add_to_cart
from pages.inventory_page import InventoryPage
import time 

def test_ui_elements(setup):
    driver, baseUrl = setup
    driver.get(baseUrl)


    perform_login_and_add_to_cart(driver)

    inventory = InventoryPage(driver)

    assert inventory.check_logo(), "logo not displayed"
    time.sleep(4)
    assert inventory.check_cart_icon(), "cart icon not displayed"
    time.sleep(4)






