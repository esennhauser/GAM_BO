from pytest_bdd import *
from pages.home_page import HomePage


@scenario('../login.feature', 'login successfully')
def test_login():
    pass


@given("we launch browser and go to GAM")
def setup_login(request, driver):
    home_page = HomePage(request.node.driver, request.node.errors)
    request.node.home_page = home_page


@when("we login with 'administrative@test.com' and 'g4mr3n0v4c10n'")
def log_in(request):
    print("\n\t\t-----Test log in-----")
    request.node.home_page.login('administrative@test.com', 'g4mr3n0v4c10n')
    request.node.inicio = request.node.home_page.select_element_by_xpath(request.node.home_page.mensaje_inicio)


@then("Bienvenido is at the top corner")
def verify_bienvenido(request):
    try:
        assert "Bienvenido" in request.node.inicio.text, "ERROR. Log in failed."
        print("Log in successful. ")
    except Exception as ex:
        request.node.errors.append(ex)
