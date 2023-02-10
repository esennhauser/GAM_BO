from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Functions.functions import Functions


class FunctionsHomePage():

    def __init__(self, driver):
        self.driver = driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.f = Functions(driver)
        self.f.go_to("https://gam-gam-renovacion-backoffice.development.mag.dev/login")

    def log_out(self, message):
        self.driver.close()
