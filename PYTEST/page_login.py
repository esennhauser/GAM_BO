from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Functions.functions import Functions


class FunctionsLogin():

    def __init__(self, driver):
        self.driver = driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.f = Functions(driver)
        self.f.go_to("https://gam-gam-renovacion-backoffice.development.mag.dev/login")
    def failed_login(self, username, password, message):
        self.f.introduce_text(":r0:", username)
        self.f.introduce_text("auth-login-password", password)
        self.f.click_by_xpath("//*[@id='__next']/div/div/div/div/div/form/button")
        error_1 = self.f.select_element_by_xpath("//*[@id='__next']/div/div/div/div/div/form/div[1]/p")
        print(error_1.text)
        if error_1.text == message:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")

    def successful_login(self, username, password, product_text):
        self.f.go_to("https://gam-gam-renovacion-backoffice.development.mag.dev/login")
        self.f.introduce_text(":r0:", username)
        self.f.introduce_text("auth-login-password", password)
        self.f.click_by_xpath("//*[@id='__next']/div/div/div/div/div/form/button")
        product_element = self.f.select_element_by_xpath("//*[@id='__next']/div/main/h3")
        if product_element.text == product_text:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")
