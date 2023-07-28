from pages.home_page import HomePage
from pytest_bdd import parsers, scenarios, given, when, then
from functools import partial
import pytest

EXTRA_TYPES = {
    'Number': int,
    'String': str,
}

scenarios('../log_out.feature')

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


@pytest.fixture(scope="function")
@given('we launch browser and go to GAM')
def setup_login(test_info):
    home_page = HomePage(test_info[0], test_info[1])
    return home_page


@when(parse_num('we login with "{username:String}" and "{password:String}"'))
@when('we login with "<username>" and "<password>"')
def wrong_username_and_wrong_password(setup_login, username, password):
    setup_login.login(username, password)


@then('Bienvenido is at the top corner')
def verify_bienvenido(setup_login, test_info):
    inicio = setup_login.select_element_by_xpath(setup_login.mensaje_inicio)
    try:
        assert "Bienvenido" in inicio.text, "ERROR. Log in failed."
        print("Log in successful. ")
    except Exception as ex:
        test_info[1].append(ex)


@then('we log out')
def log_out(setup_login):
    setup_login.log_out()


@then('I am in log in page again')
def verify_log_in_page(setup_login, test_info):
    welcome_message = setup_login.select_element_by_xpath(setup_login.mensaje_bienvenido)
    try:
        assert welcome_message.text == "Bienvenido a Gam", "ERROR. Log out failed."
        print("Log in and log out successful. ")
    except Exception as ex:
        test_info[1].append(ex)
