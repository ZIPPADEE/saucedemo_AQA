import pytest
from config.config import valid_user_1, valid_user_2, valid_user_3, invalid_user

@pytest.mark.parametrize('username, password', [
    (valid_user_1["username"], valid_user_1["password"]),
    (valid_user_2["username"], valid_user_1["password"]),
    (valid_user_3["username"], valid_user_1["password"])
])
def test_valid_login(login_page, username, password):
    login_page.open()
    login_page.login(username, password)
    assert "/inventory.html" in login_page.page.url

def test_invalid_login(login_page):
    login_page.open()
    login_page.login(invalid_user["username"], invalid_user["password"])

    assert login_page.is_error_visible(), "Not error message was displayed"

    expected_error_text = "Epic sadface: Username and password do not match any user in this service"
    actual_error = login_page.get_error_message_text()
    assert expected_error_text == actual_error, \
        f"Error message not match. Expected: '{expected_error_text}', actual: '{actual_error}'"

    login_page.close_error_message()
    assert login_page.is_error_message_disappeared(), "Error message did not disappear after clicking the close button"


def test_empty_fields(login_page):
    login_page.open()
    login_page.login("", "")

    expected_error_text = "Epic sadface: Username is required"
    actual_error = login_page.get_error_message_text()

    assert expected_error_text == actual_error, \
        f"Error message not match. Expected: '{expected_error_text}', actual: '{actual_error}'"

    login_page.close_error_message()
    assert  login_page.is_error_message_disappeared(), "Error message did not disappear after clicking the close button"

def test_locked_out_user(login_page):
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expected_error_text = "Epic sadface: Sorry, this user has been locked out."
    actual_error = login_page.get_error_message_text()

    assert expected_error_text == actual_error, \
        f"Error message not match. Expected: '{expected_error_text}', actual: '{actual_error}'"

    login_page.close_error_message()
    assert login_page.is_error_message_disappeared(), "Error message did not disappear after clicking the close button"