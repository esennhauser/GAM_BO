from pages.page_login import LoginPage
from pytest_bdd import parsers, scenarios, given, when, then
from functools import partial
import pytest

EXTRA_TYPES = {
    'Number': int,
    'String': str,
}

scenarios('../failed_logins.feature')

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


@pytest.fixture(scope="function")
@given('we launch browser and go to GAM')
def setup_login(test_info):
    login = LoginPage(test_info[0], test_info[1])
    return login


@when(parse_num('we login with "{username:String}" and "{password:String}"'))
@when('we login with "<username>" and "<password>"')
def wrong_username_and_wrong_password(setup_login, username, password):
    setup_login.login(username, password)


@then(parse_num('The error message is: "{error_message:String}"'))
@then('The error message is: "<error_message>"')
def verify_error(test_info, setup_login, error_message):
    error = setup_login.select_element_by_xpath(setup_login.username_error)
    try:
        assert error.text == error_message, print("ERROR. Unexpected error message.")
        print("Error message as expected. ")
    except Exception as ex:
        test_info[1].append(ex)
