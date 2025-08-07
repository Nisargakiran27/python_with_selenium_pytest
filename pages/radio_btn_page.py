from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()
class RadioBtn:
    """
    Page Object for the Radio Button page in DemoQA.
    Handles interactions with a single radio button element.
    """
    def __init__(self,driver):
        """
        Store the driver instance and load the radio button locator from .env.
        """
        self.driver = driver
        self.radio_btn = (By.XPATH,os.getenv("RADIO_BUTTON"))

    def open(self,baseUrl):
        """
        Navigate to the radio button page.
        Args:baseUrl (str): The base URL of the application.
        """
        self.driver.get(baseUrl + "radio-button")

    def click_radio_btn(self):
        """
        Scroll to the radio button and click it.
        """
        btn = self.driver.find_element(*self.radio_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();",btn)
        btn.click()
        time.sleep(2)

    