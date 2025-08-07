from selenium.webdriver.common.by import By
from utils.login import perform_login_and_add_to_cart
from pages.inventory import InventoryPage
import time 

def test_ui_elements(setup):
    """
    Test Case: Verify important UI elements on the Inventory Page.

    Steps:
    1. Login and land on the Inventory page using the helper function.
    2. Check if the app logo is visible.
    3. Check if the cart icon is visible.

    Expected Result:
    - App logo should be displayed.
    - Cart icon should be displayed.

    Args:
        setup (fixture): Provides initialized WebDriver instance and base URL.
    """
    driver, baseUrl = setup
    driver.get(baseUrl)


    perform_login_and_add_to_cart(driver)

    inventory = InventoryPage(driver)

    assert inventory.check_logo(), "logo not displayed"
    time.sleep(4)
    assert inventory.check_cart_icon(), "cart icon not displayed"
    time.sleep(4)






