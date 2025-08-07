from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

import time
class Checkbox:
    """
    This page is all about the checkbox feature on DemoQA.
    We store locators for the main checkbox and its sub-option here.
    """
    def __init__(self,driver):
        """
        Store the driver and load checkbox-related locators from .env.
        """
        self.driver = driver
        self.checkbox_btn = (By.XPATH,os.getenv("CHECKBOX_BUTTON"))
        self.sub_checkbox = (By.XPATH,os.getenv("CHECKBOX_SUB_ITEM"))

    def open (self,baseUrl):
        """
        Open the checkbox page using the given base URL.
        """
        # driver , baseUrl = setup
        self.driver.get(baseUrl + "checkbox")

    def select_checkbox(self):
        """
        Scroll to the main checkbox and click it.
        """
        btn = self.driver.find_element(*self.checkbox_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();",btn)
        time.sleep(2)
        btn.click()

    def select_sub_checkbox(self):
        """
        Scroll to the sub-checkbox option and click it.
        """
        btn_2 = self.driver.find_element(*self.sub_checkbox)
        self.driver.execute_script("arguments[0].scrollIntoView();",btn_2) 
        time.sleep(2)
        btn_2.click()

