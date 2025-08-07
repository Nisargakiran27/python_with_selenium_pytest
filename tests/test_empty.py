import pytest
from utils.login_data_loader import load_login_data

login_data = load_login_data()

@pytest.mark.emptyu
@pytest.mark.parametrize("username,password,expected", login_data["empty_username"])
def test_empty_username(login, username, password, expected):
    """
    Test Case: Validate login behavior when username is left empty.

    Steps:
    1. Attempt login with an empty username and provided password.
    2. Verify the application displays the correct error message.

    Assertions:
        - The error message should contain "Username is required".

    Args:
        login (fixture): Instance of the LoginPages class.
        username (str): Username from test data (empty in this case).
        password (str): Password from test data.
        expected (str): Expected error message.
    """
    login.login(username, password)
    assert "Username is required" in login.get_error_message()

@pytest.mark.emptyp
@pytest.mark.parametrize("username,password,expected", login_data["empty_password"])
def test_empty_password(login, username, password, expected):
    login.login(username, password)
    assert "Password is required" in login.get_error_message()