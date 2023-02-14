import pytest
from PYTEST.Pages.page_login import FunctionsLogin


def test_wrong_username_and_password():
    print("\n\t\t-----Test wrong username and wrong password-----")
    login_function = FunctionsLogin()
    login_function.failed_login_username_message("ernesto", "password123", "Email or Password is invalid")
    login_function.f.driver.close()

def test_empty_username_and_wrong_password():
    print("\n\t\t-----Test empty username and wrong password-----")
    login_function = FunctionsLogin()
    login_function.failed_login_username_message("", "password123", "username must be at least 6 characters")
    login_function.f.driver.close()

def test_wrong_username_and_empty_password():
    print("\n\t\t-----Test wrong username and wrong password-----")
    login_function = FunctionsLogin()
    login_function.failed_login_password_message("ernesto", "", "password must be at least 6 characters")
    login_function.f.driver.close()

def test_empty_username_and_empty_password():
    print("\t\t-----Test empty username and empty password-----")
    login_function = FunctionsLogin()
    login_function.failed_login_username_message("", "", "username must be at least 6 characters")
    login_function.f.driver.close()

def test_wrong_password():
    print("\t\t-----Test wrong password-----")
    login_function = FunctionsLogin()
    login_function.failed_login_username_message("standard_user", "password123", "Email or Password is invalid")
    login_function.f.driver.close()

