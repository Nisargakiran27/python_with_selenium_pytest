from pages.login_page import LoginPage


def perform_login_and_add_to_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")