import pytest
from Pages.page_login import LoginPage


class TestFailedLogins:
    login = ""

    @pytest.fixture
    def setup_login(self):
        self.login = LoginPage()
        yield
        self.login.browser.driver.close()

    @pytest.mark.failed_run
    @pytest.mark.usefixtures("setup_login")
    def test_wrong_username_and_password(self):
        print("\n\t\t-----Test wrong username and wrong password-----")
        self.login.login("ernesto", "password123")
        error = self.login.browser.select_element_by_xpath(self.login.username_error)
        assert error.text == "Email or Password is invalid", "ERROR. Unexpected error message."

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.failed_run
    def test_empty_username_and_wrong_password(self):
        print("\n\t\t-----Test empty username and wrong password-----")
        self.login.login("", "password123")
        error = self.login.browser.select_element_by_xpath(self.login.username_error)
        assert error.text == "username must be at least 6 characters", "ERROR. Unexpected error message."

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.failed_run
    def test_wrong_username_and_empty_password(self):
        print("\n\t\t-----Test wrong username and wrong password-----")
        self.login.login("ernesto", "")
        error = self.login.browser.select_element_by_xpath(self.login.password_error)
        assert error.text == "password must be at least 6 characters", "ERROR. Unexpected error message."

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.failed_run
    def test_empty_username_and_empty_password(self):
        print("\t\t-----Test empty username and empty password-----")
        self.login.login("", "")
        error = self.login.browser.select_element_by_xpath(self.login.username_error)
        assert error.text == "username must be at least 6 characters", "ERROR. Unexpected error message."

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.failed_run
    def test_wrong_password(self):
        print("\t\t-----Test wrong password-----")
        self.login.login("standard_user", "password123", )
        error = self.login.browser.select_element_by_xpath(self.login.username_error)
        assert error.text == "Email or Password is invalid", "ERROR. Unexpected error message."
