import pytest
from pages.radio_btn_page import RadioBtn


@pytest.mark.demoqa
def test_radio_button(setup):
    driver , baseUrl = setup
    # driver.get(baseUrl + "radio-button")

    # btn = driver.find_element(By.XPATH,"//label[@class='custom-control-label']")
    # driver.execute_script("arguments[0].scrollIntoView();",btn)
    # btn.click()
    # time.sleep(2)

    radio_btn = RadioBtn(driver)
    radio_btn.open(baseUrl)
    radio_btn.click_radio_btn()


