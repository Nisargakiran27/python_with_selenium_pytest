from pages.login import LoginPages


def perform_login_and_add_to_cart(driver):
    login = LoginPages(driver)
    login.login("standard_user", "secret_sauce")