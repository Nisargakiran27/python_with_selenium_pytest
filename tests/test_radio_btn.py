import pytest
from pages.radio_btn_page import RadioBtn


@pytest.mark.demoqa
def test_radio_button(setup):
    """
    Test Case: Verify that the radio button can be selected.

    Steps:
    1. Open the Radio Button page.
    2. Scroll to the radio button element.
    3. Click on the radio button.

    Expected Result:
    - The radio button should be selected successfully.
    - No errors should occur during the click action.

    Args:
        setup (fixture): Provides initialized WebDriver and base URL.
    """
    driver , baseUrl = setup
    # driver.get(baseUrl + "radio-button")

    # btn = driver.find_element(By.XPATH,"//label[@class='custom-control-label']")
    # driver.execute_script("arguments[0].scrollIntoView();",btn)
    # btn.click()
    # time.sleep(2)

    radio_btn = RadioBtn(driver)
    radio_btn.open(baseUrl)
    radio_btn.click_radio_btn()


