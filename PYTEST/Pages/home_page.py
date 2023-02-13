from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PYTEST.Functions.functions import Functions
from PYTEST.Pages.page_login import FunctionsLogin


class FunctionsHomePage(FunctionsLogin):

    def __init__(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.f = Functions(driver)
        self.f.go_to("https://gam-gam-renovacion-backoffice.development.mag.dev/login")

    def log_out(self, message):
        self.f.click_by_xpath("//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']")
        self.f.click_by_xpath("//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root"
                                 " MuiMenuItem-gutters css-158bkwc'][contains(.,'Cerrar sesión')]")
        welcome_message = self.f.select_element_by_xpath("//h5[contains(.,'Bienvenido a Gam')]")
        if welcome_message.text == message:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")