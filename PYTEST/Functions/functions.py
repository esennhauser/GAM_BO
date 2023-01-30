import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class Functions():

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url, delay):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Page opened: "+str(url))
        t = time.sleep(delay)
        return t

    def introduce_text(self, selector, text, delay):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, selector)
            val.clear()
            val.send_keys(text)
            print("Writing on the field {} the text -> {} ".format(selector, text))
            t = time.sleep(delay)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print(selector + "Element wasn't found")
            return t

    def click(self, selector, delay):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, selector)
            val.click()
            print("Clicking {}  ".format(selector))
            t = time.sleep(delay)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print(selector + "Element wasn't found")
            return t

    def select_element_by_xpath(self, element):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, element)))
        self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, element)
        return val