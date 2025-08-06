from selenium.webdriver.common.by import By

class FillForm:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name="", last_name="", postal_code=""):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()

    # def click_continue(self):
    #     self.driver.find_element(By.ID,"continue").click()

    # def assert_checkout_overview(self):
    #     assert "Checkout: Overview" in self.driver.page_source

    def finish_btn(self):
        btn = self.driver.find_element(By.ID,"finish")
        btn.click()

        
