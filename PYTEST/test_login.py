import pytest
from PYTEST.Pages.page_login import FunctionsLogin


class TestLogin:

    @pytest.fixture(scope="module")
    def setup_failed_logins():
        login_function = FunctionsLogin()
        print("setup finished")
        yield
        login_function.f.driver.close()

    def test_wrong_username_and_password(self, setup_failed_logins):
        print("\n\t\t-----Test wrong username and wrong password-----")
        #self.login_function.failed_login_username_message("ernesto", "password123", "Email or Password is invalid")

    def test_empty_username_and_wrong_password(self, setup_failed_logins):
        print("\n\t\t-----Test empty username and wrong password-----")
        self.login_function.failed_login_username_message("", "password123", "username must be at least 6 characters")

    def test_wrong_username_and_empty_password(self, setup_failed_logins):
        print("\n\t\t-----Test wrong username and wrong password-----")
        self.login_function.failed_login_password_message("ernesto", "", "password must be at least 6 characters")

    def test_empty_username_and_empty_password(self, setup_failed_logins):
        print("\t\t-----Test empty username and empty password-----")
        self.login_function.failed_login_username_message("", "", "username must be at least 6 characters")

    def test_wrong_password(self, setup_failed_logins):
        print("\t\t-----Test wrong password-----")
        self.login_function.failed_login_username_message("standard_user", "password123", "Email or Password is invalid")
    def test_successful_login(self, setup_failed_logins):
        print("\t\t-----Test standard_user login-----")
        self.login_function.successful_login("test_1", "Magnetico22!", "Inicio")

