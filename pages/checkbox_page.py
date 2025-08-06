from selenium.webdriver.common.by import By
import time
class Checkbox:
    def __init__(self,driver):
        self.driver = driver
        self.checkbox_btn = (By.XPATH,"//button[@class='rct-collapse rct-collapse-btn']")
        self.sub_checkbox = (By.XPATH,"//span[@class='rct-title' and text()='Desktop']")

    def open (self,baseUrl):
        # driver , baseUrl = setup
        self.driver.get(baseUrl + "checkbox")

    def select_checkbox(self):
        btn = self.driver.find_element(*self.checkbox_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();",btn)
        time.sleep(2)
        btn.click()

    def select_sub_checkbox(self):
        btn_2 = self.driver.find_element(*self.sub_checkbox)
        self.driver.execute_script("arguments[0].scrollIntoView();",btn_2) 
        time.sleep(2)
        btn_2.click()

