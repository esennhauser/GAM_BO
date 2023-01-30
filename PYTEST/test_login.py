import time
import pytest
import requests
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
from page_login import FunctionsLogin

t = 0.5

def test_many_logins():
    driver = ""
    login_function = FunctionsLogin(driver)
    print("\n\t\t-----Test wrong username and wrong password-----")
    login_function.failed_login("ernesto", "password123", "Epic sadface: Username and password do not "
                                                          "match any user in this service")

    print("\t\t-----Test empty username and empty password-----")
    login_function.failed_login("", "", "Epic sadface: Username is required")

    print("\t\t-----Test wrong password-----")
    login_function.failed_login("standard_user", "password123", "Epic sadface: Username and password do "
                                                                "not match any user in this service")

    print("\t\t-----Test standard_user login-----")
    login_function.successful_login("standard_user", "secret_sauce", "PRODUCTS")


