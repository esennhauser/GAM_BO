from pytest_bdd import *
from pages.home_page import HomePage
import pytest


@scenario('../login.feature', 'login successfully')
def test_login():
    pass


@pytest.fixture
@given("we launch browser and go to GAM")
def setup_login(test_info):
    home_page = HomePage(test_info[0], test_info[1])
    return home_page


@when("we login with 'administrative@test.com' and 'g4mr3n0v4c10n'")
def log_in(setup_login):
    print("\n\t\t-----Test log in-----")
    setup_login.login('administrative@test.com', 'g4mr3n0v4c10n')


@then("Bienvenido is at the top corner")
def verify_bienvenido(setup_login, test_info):
    inicio = setup_login.select_element_by_xpath(setup_login.mensaje_inicio)
    try:
        assert "Bienvenido" in inicio.text, "ERROR. Log in failed."
        print("Log in successful. ")
    except Exception as ex:
        test_info[1].append(ex)
