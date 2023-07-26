from pages.page_login import LoginPage
from pytest_bdd import parsers, scenarios, given, when, then
from functools import partial

scenarios('../failed_logins.feature')

EXTRA_TYPES = {
    'Number': int,
    'String': str,
}

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


@given('we launch browser and go to GAM')
def setup_login(request, driver):
    login = LoginPage(request.node.driver, request.node.errors)
    request.node.login = login


@when(parse_num("we login with '{username:String}' and '{password:String}'"))
def wrong_username_and_wrong_password(request, username, password):
    request.node.login.login(username, password)


@then(parse_num('The error message is: "{error_message:String}"'))
def verify_error(request, error_message):
    error = request.node.login.select_element_by_xpath(request.node.login.username_error)
    try:
        assert error.text == error_message, "ERROR. Unexpected error message."
        print("Error message as expected. ")
    except Exception as ex:
        request.node.errors.append(ex)