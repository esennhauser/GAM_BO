import pytest
from pages.page_login import LoginPage


@pytest.fixture(autouse=True, scope="class")
def setup_login(test_info):
    login = LoginPage(test_info[0], test_info[1])
    return login


class TestWrongUsernameAndWrongPassword:
    def test_wrong_username_and_wrong_password(self, setup_login, test_info):
        print("\n\t\t-----Test wrong username and wrong password-----")
        setup_login.login("ernesto", "password123")
        error = setup_login.select_element_by_xpath(setup_login.username_error)
        try:
            assert error.text == "Email or Password is invalid", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)


class TestEmptyUsernameAndWrongPassword:
    def test_empty_username_and_wrong_password(self, setup_login, test_info):
        print("\n\t\t-----Test empty username and wrong password-----")
        setup_login.login("", "password123")
        error = setup_login.select_element_by_xpath(setup_login.username_error)
        try:
            assert error.text == "username must be at least 6 characters", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)


class TestWrongUsernameAndEmptyPassword:
    def test_wrong_username_and_empty_password(self, setup_login, test_info):
        print("\n\t\t-----Test wrong username and wrong password-----")
        setup_login.login("ernesto", "")
        error = setup_login.select_element_by_xpath(setup_login.password_error)
        try:
            assert error.text == "password must be at least 6 characters", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)


class TestEmptyUsernameAndEmptyPassword:
    def test_empty_username_and_empty_password(self, setup_login, test_info):
        print("\t\t-----Test empty username and empty password-----")
        setup_login.login("", "")
        error = setup_login.select_element_by_xpath(setup_login.username_error)
        try:
            assert error.text == "username must be at least 6 characters", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)


class TestWrongPassword:
    def test_wrong_password(self, setup_login, test_info):
        print("\t\t-----Test wrong password-----")
        setup_login.login("standard_user", "password123", )
        error = setup_login.select_element_by_xpath(setup_login.username_error)
        try:
            assert error.text == "Email or Password is invalid", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)