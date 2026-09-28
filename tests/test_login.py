import pytest
from pages.login_page import LoginPage
from test_data.users import STANDARD_USER
def test_successful_login(login_page):

    login_page.load()

    login_page.login(
        STANDARD_USER["username"],
        STANDARD_USER["password"]
    )

    print(login_page.page.url)

    assert login_page.is_logged_in()
  

@pytest.mark.parametrize("username,password",[
    ("Admin","wrongpassword"),
    ("wronguser", "admin123"),
    ("231", "admin123"),

])
def test_invalid_login(login_page,username,password):
    login_page.load()
    login_page.login(username,password)
    assert login_page.get_error_message() == "Invalid credentials"


@pytest.mark.parametrize("username,password",[
    ("", "admin123"),
    ("Admin", "")])
def test_empty_username_and_password(login_page,username,password):
    login_page.load()
    login_page.login(username,password)
    assert login_page.get_required_message() == "Required"