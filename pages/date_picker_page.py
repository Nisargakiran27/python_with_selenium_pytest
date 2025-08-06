from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
class DatePicker:
    def __init__(self, driver):
        self.driver = driver
        self.date_input = (By.ID,"datePickerMonthYearInput")
        self.month_dropdown = (By.XPATH,"//select[@class='react-datepicker__month-select']")
        self.year_dropdown = (By.XPATH,"//select[@class='react-datepicker__year-select']")
        


    def open(self,baseUrl):
        self.driver.get(baseUrl + "date-picker")

    def select_dates(self,month_value,day_value,year_value):
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
