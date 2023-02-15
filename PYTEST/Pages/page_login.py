from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from PYTEST.Functions.functions import Functions


class LoginPage(Functions):

    username_textbox =":r0:"
    password_textbox = "auth-login-password"
    login_button ="//*[@id='__next']/div/div/div/div/div/form/button"
    username_error = "//*[@id='__next']/div/div/div/div/div/form/div[1]/p"
    password_error = "//p[@id='']"
    mensaje_bienvenido = "//h5[contains(.,'Bienvenido a Gam')]"

    def __init__(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser = Functions(driver)
        self.browser.go_to("https://gam-gam-renovacion-backoffice.development.mag.dev/login")

    def login(self, username, password):
        self.browser.introduce_text_by_xpath(self.username_textbox, username)
        self.browser.introduce_text_by_xpath(self.password_textbox, password)
        self.browser.click_by_xpath(self.login_button)

