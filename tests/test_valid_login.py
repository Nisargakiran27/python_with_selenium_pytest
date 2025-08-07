import pytest
from utils.login_data_loader import load_login_data


login_data = load_login_data()

@pytest.mark.valid
@pytest.mark.parametrize("username,password,expected",login_data["valid"])
def test_valid_login(login,username, password,expected):
    """
    Test Case: Login with valid credentials.

    Steps:
    1. Enter a valid username and password from the test data.
    2. Submit the login form.

    Expected Result:
    - User should be redirected to the inventory page.
    - URL should contain 'inventory'.

    Args:
        login (fixture): Provides a LoginPages instance with WebDriver.
        username (str): Valid username from test data.
        password (str): Valid password from test data.
        expected (str): Expected outcome description from test data.
    """
    login.login(username,password)
    assert "inventory"in login.driver.current_url

    
