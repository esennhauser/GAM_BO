import pytest
from PYTEST.Pages.home_page import HomePage

def users_Data():
    return [
        ("test_1","Magnetico22!"),
        ("staff1", "Magnetico22!"),
        ("administrador_general", "Magnetico22!"),
        ("administrativo1", "Magnetico22!"),
        ("ecommerce1", "Magnetico22!"),
        ("managerzonal1", "Magnetico22!"),
        ("managergba", "Magnetico22!"),
        ("logistica1", "Magnetico22!"),
        ("vendedor4", "Magnetico22!")

    ]


@pytest.fixture
def setup_login():
    global function_home_page
    function_home_page = HomePage()


@pytest.mark.login_logout
@pytest.mark.parametrize("username,password", users_Data())
def test_log_out_admin_user(username, password):
    print("\n\t\t-----Test log out for Admin user-----")
    function_home_page.login(username, password)
    inicio = function_home_page.browser.select_element_by_xpath(function_home_page.mensaje_inicio)
    assert inicio.text == "Inicio", "ERROR. Log in failed."
    function_home_page.log_out()
    welcome_message = function_home_page.browser.select_element_by_xpath(function_home_page.mensaje_bienvenido)
    assert welcome_message.text == "Bienvenido a Gam", "ERROR. Log out failed."


def teardown_function():
    function_home_page.browser.driver.close()