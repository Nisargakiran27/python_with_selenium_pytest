from selenium.webdriver.common.by import By
import time

class RadioBtn:
    def __init__(self,driver):
        self.driver = driver
        self.radio_btn = (By.XPATH,"//label[@class='custom-control-label']")

    def open(self,baseUrl):
        self.driver.get(baseUrl + "radio-button")

    def click_radio_btn(self):
        btn = self.driver.find_element(*self.radio_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();",btn)
        btn.click()
        time.sleep(2)

    