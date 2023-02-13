from Functions.functions import Functions
from PYTEST.Pages.page_login import FunctionsLogin
from PYTEST.Pages.home_page import FunctionsHomePage


def test_log_out_admin_user():
    driver = ""
    print("\n\t\t-----Test log out-----")
    function_home_page = FunctionsHomePage(driver)
    function_home_page.successful_login("test_1", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()
