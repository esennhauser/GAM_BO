import pytest
from Pages.home_page import HomePage

def users_Data():
    return [
        ("administrative@test.com","g4mr3n0v4c10n"),
        ("client@test.com", "g4mr3n0v4c10n"),
        ("ecommerce@test.com", "g4mr3n0v4c10n"),
        ("general_administrator@test.com", "g4mr3n0v4c10n"),
        ("logistic@test.com", "g4mr3n0v4c10n"),
        ("manager_gba@test.com", "g4mr3n0v4c10n"),
        ("manager_zonal@test.com", "g4mr3n0v4c10n"),
        ("staff@test.com", "g4mr3n0v4c10n"),
        ("admin@guialemor.com", "g4mr3n0v4c10n")

    ]


@pytest.fixture
def setup_login():
    global function_home_page
    function_home_page = HomePage()


@pytest.mark.login_logout
@pytest.mark.parametrize("username,password", users_Data())
def test_log_out_admin_user(setup_login, username, password):
    print("\n\t\t-----Test log out for Admin user-----")
    function_home_page.login(username, password)
    inicio = function_home_page.browser.select_element_by_xpath(function_home_page.mensaje_inicio)
    assert inicio.text == "Inicio", "ERROR. Log in failed."
    function_home_page.log_out()
    welcome_message = function_home_page.browser.select_element_by_xpath(function_home_page.mensaje_bienvenido)
    assert welcome_message.text == "Bienvenido a Gam", "ERROR. Log out failed."


def teardown_function():
    function_home_page.browser.driver.close()