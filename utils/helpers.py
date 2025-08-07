from pages.login import LoginPages
from pages.inventory import InventoryPage

def perform_login_and_add_to_cart(driver):
    login = LoginPages(driver)
    login.login("standard_user", "secret_sauce")
    Inventory = InventoryPage(driver)
    Inventory.click_random_product()
    Inventory.click_add_to_cart()
    Inventory.click_cart_icon()


