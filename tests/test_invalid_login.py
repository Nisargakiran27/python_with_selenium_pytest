import pytest
from utils.login_data_loader import load_login_data

login_data = load_login_data()


@pytest.mark.invalid
@pytest.mark.parametrize("username,password,expected", login_data["invalid"])
def test_invalid_login(login,username,password,expected):
    """
    Test Case: Verify login behavior with invalid credentials.

    Steps:
    1. Attempt to log in using a username and password from the invalid credentials dataset.
    2. Capture the error message displayed on the login page.

    Expected Result:
    - The system should display an error message indicating that the user is locked out 
      or credentials are invalid.
    - The login attempt should fail, and the user should remain on the login page.

    Args:
        login (fixture): LoginPages POM instance for interacting with the login screen.
        username (str): Username from test data.
        password (str): Password from test data.
        expected (str): Expected error message (e.g., "locked out").
    """
    login.login(username,password)
    assert "locked out" in login.get_error_message()