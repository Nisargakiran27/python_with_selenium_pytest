import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import os 
import time



@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Disable save password prompt
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)
    ser_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=ser_obj, options=chrome_options)
    driver.maximize_window()
    if request.node.get_closest_marker("demoqa"):
        baseUrl = "https://demoqa.com/"
    else:
        baseUrl = "https://www.saucedemo.com/"

    yield driver ,baseUrl

    driver.quit()
@pytest.fixture
def login_page(setup):
    driver, base_url = setup
    page = LoginPage(driver)
    page.open(base_url)
    return page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver_tuple = item.funcargs.get("setup")
        if driver_tuple:
            driver = driver_tuple[0]
            test_name = item.name
            os.makedirs("screenshots", exist_ok=True)
            filename = f"{test_name}_{int(time.time())}.png"
            filepath = os.path.join("screenshots", filename)
            driver.save_screenshot(filepath)
            print(f"\n Screenshot saved at: {filepath}")
