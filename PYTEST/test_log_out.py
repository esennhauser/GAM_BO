from Functions.functions import Functions
from page_login import FunctionsLogin
from home_page import FunctionsHomePage


def test_log_out_admin_user():
    driver = ""
    functions_login = FunctionsLogin(driver)
    functions_login.successful_login("test_1", "Magnetico22!", "Inicio")
    functions = Functions(driver)
    functions.click_by_xpath("//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']"
                             "[contains(.,'ES')]")
    functions.click_by_xpath("//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root"
                             " MuiMenuItem-gutters css-158bkwc'][contains(.,'Cerrar sesión')]")
    welcome_message = functions.select_element_by_xpath("//h5[contains(.,'Bienvenido a Gam')]")
    if welcome_message.text == "Bienvenido a Gam":
        print("\t\t-----PASSED-----\n\n")
    else:
        print("\t\t-----FAILED-----\n\n")