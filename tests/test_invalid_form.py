import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.form_filling import FillForm
import time
from utils.helpers import perform_login_and_add_to_cart
from utils.read_form_csv import read_form_login_data

form_data = read_form_login_data("test_data\\form_data.csv")



@pytest.mark.parametrize("data",form_data)
def test_invalid_form_filling(setup, data):
    driver , baseUrl = setup

    driver.get(baseUrl)

    perform_login_and_add_to_cart(driver)

    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(2)


    form = FillForm(driver)

    form.fill_form(
        first_name = data.get("first_name"),
        last_name = data.get("last_name"),
        postal_code= data.get("postal_code")
    )

    form.click_continue()
    time.sleep(2)




