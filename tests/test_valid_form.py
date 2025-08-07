from pages.login import LoginPages
from pages.inventory import InventoryPage
from utils.helpers import perform_login_and_add_to_cart
from pages.cart_page import CartPage
from pages.form_filling import FillForm
import time

# def test_valid_form_fill(setup):
#     driver ,  baseUrl = setup
#     driver.get(baseUrl)

#     perform_login_and_add_to_cart(driver)
#     cart = CartPage(driver)
#     cart.click_checkout()
#     time.sleep(2)

#     form = FillForm(driver)
#     form.fill_form()
#     time.sleep(2)
#     form.click_continue()

   
#     # form.assert_checkout_overview()
#     form.finish_btn()

from utils.valid_form import read_from_valid_form_data  # create a utility for CSV reading

def test_valid_form_fill(setup):
    """
    Test Case: Fill the checkout form with valid details and complete the purchase.

    Steps:
    1. Login and add a product to the cart.
    2. Go to the cart page and click checkout.
    3. Read valid user details from CSV.
    4. Fill in the checkout form with the details.
    5. Continue to the next step and click the finish button.

    Expected Result:
    - Checkout form should accept valid details.
    - Purchase flow should proceed to the finish stage without errors.

    Args:
        setup (fixture): Provides initialized WebDriver instance and base URL.
    """
    driver, baseUrl = setup
    driver.get(baseUrl)

    perform_login_and_add_to_cart(driver)
    cart = CartPage(driver)
    cart.click_checkout()
    time.sleep(2)

    data = read_from_valid_form_data("test_data\\valid_form_data.csv")[0]  # first row from CSV
    form = FillForm(driver)
    # form.fill_form(data["first_name"], data["last_name"], data["postal_code"])
    form.fill_form(**data)
    time.sleep(2)
    form.click_continue()
    form.finish_btn()
