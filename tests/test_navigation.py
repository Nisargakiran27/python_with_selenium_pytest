import pytest
from pages.menu_page import MenuPage
from utils.login import perform_login_and_add_to_cart
import time

def test_navigation_links(setup):
    driver , baseUrl = setup
    driver.get(baseUrl)

    perform_login_and_add_to_cart(driver)

    menu_bar = MenuPage(driver)
    # menu_bar.open_hamberger_menu()
    # time.sleep(2)
    # menu_bar.click_all_item()
    menu_bar.click_twitter()
    time.sleep(6)

