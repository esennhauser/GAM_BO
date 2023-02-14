from Functions.functions import Functions
import pytest
from PYTEST.Pages.page_login import FunctionsLogin
from PYTEST.Pages.home_page import FunctionsHomePage

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
@pytest.mark.login_logout
@pytest.mark.parametrize("username,password", users_Data())
def test_log_out_admin_user(username, password):
    print("\n\t\t-----Test log out for Admin user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login(username, password, "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()
