import pytest
from pages.menu_page import MenuPage
from utils.login import perform_login_and_add_to_cart
import time

def test_navigation_links(setup):
    """
    Test Case: Verify navigation through menu links.

    Steps:
    1. Open the application base URL.
    2. Perform a valid login and land on the inventory page.
    3. Access the menu bar options.
    4. Click the Twitter link from the menu.

    Expected Result:
    - Clicking the Twitter link should open the official Twitter page 
      in a new tab/window.
    - The current browser session should remain active.

    Args:
        setup (fixture): Provides initialized WebDriver and base URL.
    """
    driver , baseUrl = setup
    driver.get(baseUrl)

    perform_login_and_add_to_cart(driver)

    menu_bar = MenuPage(driver)
    # menu_bar.open_hamberger_menu()
    # time.sleep(2)
    # menu_bar.click_all_item()
    menu_bar.click_twitter()
    time.sleep(6)

