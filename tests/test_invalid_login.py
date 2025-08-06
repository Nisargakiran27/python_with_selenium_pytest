import pytest
from utils.login_data_loader import load_login_data

login_data = load_login_data()


@pytest.mark.invalid
@pytest.mark.parametrize("username,password,expected", login_data["invalid"])
def test_invalid_login(login_page,username,password,expected):
    login_page.login(username,password)
    assert "locked out" in login_page.error_message()