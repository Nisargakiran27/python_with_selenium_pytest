import pytest
from utils.login_data_loader import load_login_data

login_data = load_login_data()

@pytest.mark.emptyu
@pytest.mark.parametrize("username,password,expected", login_data["empty_username"])
def test_empty_username(login_page, username, password, expected):
    login_page.login(username, password)
    assert "Username is required" in login_page.error_message()

@pytest.mark.emptyp
@pytest.mark.parametrize("username,password,expected", login_data["empty_password"])
def test_empty_password(login_page, username, password, expected):
    login_page.login(username, password)
    assert "Password is required" in login_page.error_message()