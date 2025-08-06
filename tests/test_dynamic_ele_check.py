import pytest
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.login import perform_login_and_add_to_cart

def test_dynamic_elements(setup):
    driver , baseUrl = setup
    driver.get(baseUrl)

    perform_login_and_add_to_cart(driver)
    inventory = InventoryPage(driver)

    inventory.click_random_product()
    inventory.click_add_to_cart()
    inventory.click_cart_icon()


    assert inventory.cart_badge_check() is True , "Badge not displayed"

    assert inventory.badge_count() == "1", "Badge count is not 1"
