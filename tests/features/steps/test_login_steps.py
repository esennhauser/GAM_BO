from pytest_bdd import *
import pytest
from pages.home_page import HomePage


@scenario('../login.feature', 'login successfully')
def test_login():
    pass


@given("we launch browser and go to GAM")
@pytest.fixture(autouse=True)
def setup_login(request, driver):
    home_page = HomePage(request.cls.driver, request.cls.errors)
    request.cls.home_page = home_page


@when("we login with 'administrative@test.com' and 'g4mr3n0v4c10n'")
def log_in(self):
    print("\n\t\t-----Test log in-----")
    self.home_page.login('administrative@test.com', 'g4mr3n0v4c10n')
    inicio = self.home_page.select_element_by_xpath(self.home_page.mensaje_inicio)


@then("Bienvenido is at the top corner")
def verify_bienvenido(self):
    try:
        assert "Bienvenido" in inicio.text, "ERROR. Log in failed."
        print("Log in successful. ")
    except Exception as ex:
        self.errors.append(ex)
