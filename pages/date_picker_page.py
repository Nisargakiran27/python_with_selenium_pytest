from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
import os 
import time

load_dotenv()

class DatePicker:
    """
    This page object is for handling the date picker on DemoQA.
    It helps in selecting month, day, and year from the calendar.
    """
    def __init__(self, driver):
        """
        Store the driver and load date picker locators from .env.
        """
        self.driver = driver
        self.date_input = (By.ID,os.getenv("DATE_INPUT"))
        self.month_dropdown = (By.XPATH,os.getenv("DATE_MONTH_DROPDOWN"))
        self.year_dropdown = (By.XPATH,os.getenv("DATE_YEAR_DROPDOWN"))
        


    def open(self,baseUrl):
        """
        Open the date picker page using the given base URL.
        """
        self.driver.get(baseUrl + "date-picker")

    def select_dates(self,month_value,day_value,year_value):
        """
        Select a date by choosing the year, month, and day from the date picker.
        Prints the selected date at the end.
        """
        input = self.driver.find_element(*self.date_input)
        self.driver.execute_script("arguments[0].scrollIntoView();",input)
        input.click()

        year = Select(self.driver.find_element(*self.year_dropdown))
        year.select_by_visible_text(year_value)
        time.sleep(2)

        month = Select(self.driver.find_element(*self.month_dropdown))
        month.select_by_visible_text(month_value)
        time.sleep(2)

        day = self.driver.find_element(By.XPATH,f"//div[text()='{day_value}']")
        self.driver.execute_script("arguments[0].scrollIntoView();",day)
        time.sleep(2)
        day.click()
        time.sleep(2)
        

        print("My Birthday : ", input.get_attribute("value"))
