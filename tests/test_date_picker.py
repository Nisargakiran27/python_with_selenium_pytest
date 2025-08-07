import pytest
from pages.date_picker_page import DatePicker
from utils.datepicker import datepicker


date_data = datepicker("test_data\\date_picker.csv")

@pytest.mark.demoqa
@pytest.mark.parametrize("month,day,year", date_data)
def test_date_picker(setup, month , day , year):
    """
    Test Case: Select a date from the DemoQA Date Picker widget.

    Steps:
    1. Open the DemoQA date picker page.
    2. Select the given year from the dropdown.
    3. Select the given month from the dropdown.
    4. Select the given day from the calendar.
    5. Verify the selected date is entered in the input field.

    Args:
        setup (fixture): Provides WebDriver instance and base URL.
        month (str): Month to select from the dropdown.
        day (str): Day to select from the calendar.
        year (str): Year to select from the dropdown.
    """
    driver , baseUrl = setup
    driver.get(baseUrl + "date-picker")


    date_picker = DatePicker(driver)
    date_picker.open(baseUrl)
    date_picker.select_dates(month,day,year)


    

