import pytest
from selenium.webdriver.common.by import By
from utils.read_csv import read_login_data, filter_data_by_type


# Load and filter data
all_data = read_login_data("test_data/login_data.csv")
valid_data = filter_data_by_type(all_data, "success")
invalid_data = filter_data_by_type(all_data, "failure")
empty_username_data = filter_data_by_type(all_data, "empty_username")
empty_password_data = filter_data_by_type(all_data, "empty_password")

@pytest.mark.valid
@pytest.mark.parametrize("username,password,expected", valid_data)
def test_valid_login(setup, username, password, expected):
    driver, baseUrl = setup
    driver.get(baseUrl)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url


@pytest.mark.invalid
@pytest.mark.parametrize("username,password,expected", invalid_data)
def test_invalid_login(setup, username, password, expected):
    driver, baseUrl = setup
    driver.get(baseUrl)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    error_text = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "locked out" in error_text.lower()


@pytest.mark.emptyu
@pytest.mark.parametrize("username,password,expected", empty_username_data)
def test_empty_username(setup, username, password, expected):
    driver, baseUrl = setup
    driver.get(baseUrl)
    if username:
        driver.find_element(By.ID, "user-name").send_keys(username)
    if password:
        driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    error_text = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username is required" in error_text


@pytest.mark.emptyp
@pytest.mark.parametrize("username,password,expected", empty_password_data)
def test_empty_password(setup, username, password, expected):
    driver, baseUrl = setup
    driver.get(baseUrl)
    if username:
        driver.find_element(By.ID, "user-name").send_keys(username)
    if password:
        driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    error_text = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Password is required" in error_text


