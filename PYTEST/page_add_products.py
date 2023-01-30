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


class FunctionsAddProducts():

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self, selector, message, t=0.5):
        f = Functions(self.driver)
        f.click("add-to-cart-sauce-labs-backpack", t)
        button = f.select_element_by_xpath(selector)
        if button.text == message:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")