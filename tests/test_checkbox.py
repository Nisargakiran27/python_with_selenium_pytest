import pytest
from selenium.webdriver.common.by import By
from pages.checkbox_page import Checkbox

import time 

# @pytest.mark.demoqa
# def test_checkbox(setup):
#     driver , baseUrl = setup
#     driver.get(baseUrl + "checkbox")

#     btn = driver.find_element(By.XPATH,"//button[@class='rct-collapse rct-collapse-btn']")
#     driver.execute_script("arguments[0].scrollIntoView();",btn)
#     btn.click()
#     time.sleep(2)
#     checkbox = driver.find_element(By.XPATH,"//span[@class='rct-title' and text()='Desktop']")
#     checkbox.click()
#     time.sleep(2)



@pytest.mark.demoqa
def test_checkbox(setup):
    driver , baseUrl = setup

    check_box = Checkbox(driver)
    check_box.open(baseUrl)
    check_box.select_checkbox()
    check_box.select_sub_checkbox()

