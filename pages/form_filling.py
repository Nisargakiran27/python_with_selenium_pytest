from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

class FillForm:
    """
    This page object is for the checkout form in Saucedemo.
    It handles entering customer details and continuing to the next step.
    """
    def __init__(self, driver):
        """
        Store the driver and load all form-related locators from .env.
        """
        self.driver = driver
        self.form_firstname = (By.ID,os.getenv("FORM_FIRST_NAME"))
        self.form_lastname = (By.ID,os.getenv("FORM_LAST_NAME"))
        self.form_postal_code = (By.ID,os.getenv("FORM_POSTAL_CODE"))
        self.continue_btn = (By.ID,os.getenv("CONTINUE_BTN"))
        self.finish_btnn = (By.ID,os.getenv("FINISH_BTN"))


    def fill_form(self, first_name="", last_name="", postal_code=""):
        """
        Fill in the form with first name, last name, and postal code.
        """
        self.driver.find_element(*self.form_firstname).send_keys(first_name)
        self.driver.find_element(*self.form_lastname).send_keys(last_name)
        self.driver.find_element(*self.form_postal_code).send_keys(postal_code)

    def click_continue(self):
        """
        Click the 'Continue' button to proceed with the checkout.
        """
        self.driver.find_element(*self.continue_btn).click()

    # def click_continue(self):
    #     self.driver.find_element(By.ID,"continue").click()

    # def assert_checkout_overview(self):
    #     assert "Checkout: Overview" in self.driver.page_source

    def finish_btn(self):
        """
        Click the 'Finish' button to complete the checkout process.
        """
        btn = self.driver.find_element(*self.finish_btnn)
        btn.click()

        
