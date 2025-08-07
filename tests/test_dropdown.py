import pytest 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@pytest.mark.demoqa
def test_dropdown(setup):
    """
    Test Case: Select an option from the DemoQA Select Menu (Dropdown).

    Steps:
    1. Open the DemoQA "Select Menu" page.
    2. Scroll to the first dropdown element.
    3. Click to open the dropdown.
    4. Select "Group 1, option 2" from the dropdown list.
    5. Pause for visibility (manual verification/demo).

    Args:
        setup (fixture): Provides WebDriver instance and base URL.
    """
    driver , baseUrl = setup
    driver.get(baseUrl + "select-menu")

    dropdown1 = driver.find_element(By.CLASS_NAME,"css-1hwfws3")
    driver.execute_script("arguments[0].scrollIntoView();",dropdown1)
    dropdown1.click()
    driver.find_element(By.XPATH, "//div[text()='Group 1, option 2']").click()
    time.sleep(4)

    # dropdown2 = driver.find_element(By.XPATH,"(//div[@class='mt-4 row'])[1]")
    # driver.execute_script("arguments[0].scrollIntoView();",dropdown2)
    # dropdown2.click()
    # driver.find_element(By.XPATH,"//div[text()='Mr.']").click()
    # time.sleep(2)

    



    