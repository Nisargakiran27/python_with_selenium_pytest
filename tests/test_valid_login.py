import pytest
from utils.login_data_loader import load_login_data

login_data = load_login_data()

@pytest.mark.valid
@pytest.mark.parametrize("username,password,expected",login_data["valid"])
def test_valid_login(login_page,username, password,expected):
    login_page.login(username,password)
    assert "inventory"in login_page.driver.current_url

    
