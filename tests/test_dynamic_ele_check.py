import pytest
from selenium.webdriver.common.by import By
from pages.inventory import InventoryPage
from pages.login import LoginPages
from utils.login import perform_login_and_add_to_cart

def test_dynamic_elements(setup):
    """
    Test Case: Verify dynamic elements like cart badge and count in the inventory page.

    Steps:
    1. Open the SauceDemo login page.
    2. Log in using the `perform_login_and_add_to_cart` helper method.
    3. On the inventory page, click a random product.
    4. Add the product to the cart.
    5. Open the cart by clicking the cart icon.
    6. Verify the cart badge is displayed.
    7. Verify the badge count equals "1".

    Assertions:
        - Cart badge should be visible after adding a product.
        - Cart badge count should match "1".

    Args:
        setup (fixture): Provides the WebDriver instance and base URL.
    """
    driver , baseUrl = setup
    driver.get(baseUrl)

    perform_login_and_add_to_cart(driver)
    inventory = InventoryPage(driver)

    inventory.click_random_product()
    inventory.click_add_to_cart()
    inventory.click_cart_icon()


    assert inventory.cart_badge_check() is True , "Badge not displayed"

    assert inventory.badge_count() == "1", "Badge count is not 1"
