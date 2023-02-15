from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PYTEST.Functions.functions import Functions
from PYTEST.Pages.page_login import LoginPage


class HomePage(LoginPage):
    avatar = "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']"
    cerrar_sesion = "//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-" \
                    "rootMuiMenuItem-gutters css-158bkwc'][contains(.,'Cerrar sesión')]"
    mensaje_inicio = "//*[@id='__next']/div/main/h3"

    def __init__(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser = Functions(driver)
        self.browser.go_to("https://gam-gam-renovacion-backoffice.development.mag.dev/login")

    def log_out(self):
        self.browser.click_by_xpath(self.avatar)
        self.browser.click_by_xpath(self.cerrar_sesion)

