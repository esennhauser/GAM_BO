import time
import pytest

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
from page_add_products import FunctionsAddProducts

t = 0.5
driver = ""

def setup_function(function):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    f = Functions(driver)
    f.go_to("https://www.saucedemo.com/", t)
    f.introduce_text("user-name", "standard_user", t)
    f.introduce_text("password", "secret_sauce", t)
    f.click("login-button", t)
    print("\n\t\t -----Logging in with standard_user----- \n")

def teardown_function(function):
    print("\n\t\t Test Add One Product finished \n")
    driver.close()

def test_add_one_product():
    add_product_function = FunctionsAddProducts(driver)
    print("\n\t\t-----Test add one product-----")
    add_product_function.add_backpack("//*[@id='remove-sauce-labs-backpack']", "REMOVE")
