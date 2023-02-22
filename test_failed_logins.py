import pytest
from Pages.page_login import LoginPage
import allure
from allure_commons.types import AttachmentType


@pytest.fixture
def setup_login():
    global login_function
    login_function = LoginPage()


def teardown_function():
    login_function.browser.driver.close()


@pytest.mark.failed_run
def test_wrong_username_and_password(setup_login):
    print("\n\t\t-----Test wrong username and wrong password-----")
    login_function.login("ernesto", "password123")
    allure.attach(login_function.browser.driver.get_screenshot_as_png(), name="user",
                  attachment_type=AttachmentType.PNG)
    error = login_function.browser.select_element_by_xpath(login_function.username_error)
    assert error.text == "Email or Password is invalid", "ERROR. Unexpected error message."


@pytest.mark.failed_run
def test_empty_username_and_wrong_password(setup_login):
    print("\n\t\t-----Test empty username and wrong password-----")
    login_function.login("", "password123")
    error = login_function.browser.select_element_by_xpath(login_function.username_error)
    assert error.text == "username must be at least 6 characters", "ERROR. Unexpected error message."


@pytest.mark.failed_run
def test_wrong_username_and_empty_password(setup_login):
    print("\n\t\t-----Test wrong username and wrong password-----")
    login_function.login("ernesto", "")
    error = login_function.browser.select_element_by_xpath(login_function.password_error)
    assert error.text == "password must be at least 6 characters", "ERROR. Unexpected error message."


@pytest.mark.failed_run
def test_empty_username_and_empty_password(setup_login):
    print("\t\t-----Test empty username and empty password-----")
    login_function.login("", "")
    error = login_function.browser.select_element_by_xpath(login_function.username_error)
    assert error.text == "username must be at least 6 characters", "ERROR. Unexpected error message."


@pytest.mark.failed_run
def test_wrong_password(setup_login):
    print("\t\t-----Test wrong password-----")
    login_function.login("standard_user", "password123", )
    error = login_function.browser.select_element_by_xpath(login_function.username_error)
    assert error.text == "Email or Password is invalid", "ERROR. Unexpected error message."
