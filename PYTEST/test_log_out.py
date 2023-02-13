from Functions.functions import Functions
from PYTEST.Pages.page_login import FunctionsLogin
from PYTEST.Pages.home_page import FunctionsHomePage


def test_log_out_admin_user():
    print("\n\t\t-----Test log out for Admin user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("test_1", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()

def test_log_out_staff_user():
    print("\n\t\t-----Test log out for Staff user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("staff1", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()

def test_log_out_general_admin():
    print("\n\t\t-----Test log out for General Admin user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("administrador_general", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()

def test_log_out_administrative():
    print("\n\t\t-----Test log out for Administrative user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("administrativo1", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()


def test_log_out_ecommerce():
    print("\n\t\t-----Test log out for Ecommerce user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("ecommerce1", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()


def test_log_out_zonal_manager():
    print("\n\t\t-----Test log out for zonal manager user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("managerzonal1", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()


def test_log_out_manager_gba():
    print("\n\t\t-----Test log out for GBA Manager user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("managergba", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()


def test_log_out_logistic():
    print("\n\t\t-----Test log out for Logistic user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("logistica1", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()


def test_log_out_salesman():
    print("\n\t\t-----Test log out for Salesman user-----")
    function_home_page = FunctionsHomePage()
    function_home_page.successful_login("vendedor4", "Magnetico22!", "Inicio")
    function_home_page.log_out("Bienvenido a Gam")
    function_home_page.f.driver.close()

