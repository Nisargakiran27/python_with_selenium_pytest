from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def perform_login_and_add_to_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    Inventory = InventoryPage(driver)
    Inventory.click_random_product()
    Inventory.click_add_to_cart()
    Inventory.click_cart_icon()


