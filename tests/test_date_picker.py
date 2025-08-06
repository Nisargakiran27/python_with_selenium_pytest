import pytest
from pages.date_picker_page import DatePicker
from utils.datepicker import datepicker


date_data = datepicker("test_data\\date_picker.csv")

@pytest.mark.demoqa
@pytest.mark.parametrize("month,day,year", date_data)
def test_date_picker(setup, month , day , year):
    driver , baseUrl = setup
    driver.get(baseUrl + "date-picker")


    date_picker = DatePicker(driver)
    date_picker.open(baseUrl)
    date_picker.select_dates(month,day,year)


    

