import time

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

    def failed_login(self, username, password, message, t=0.1):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        f = Functions(driver)
        f.go_to("https://www.saucedemo.com/", t)
        f.introduce_text("user-name", username, t)
        f.introduce_text("password", password, t)
        f.click("login-button", t)
        error_1 = f.select_element_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3")
        print(error_1.text)
        if error_1.text == message:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")
        driver.close()

    def successful_login(self, username, password, product_text, t=0.1):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        f = Functions(driver)
        f.go_to("https://www.saucedemo.com/", t)
        f.introduce_text("user-name", username, t)
        f.introduce_text("password", password, t)
        f.click("login-button", t)
        product_element = f.select_element_by_xpath("// *[ @ id = 'header_container'] / div[2] / span")
        if product_element.text == product_text:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")
        driver.close()

    def successful_login_opened(self, username, password, product_text, t=0.1):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        f = Functions(driver)
        f.go_to("https://www.saucedemo.com/", t)
        f.introduce_text("user-name", username, t)
        f.introduce_text("password", password, t)
        f.click("login-button", t)
        product_element = f.select_element_by_xpath("// *[ @ id = 'header_container'] / div[2] / span")
        if product_element.text == product_text:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")
