import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Functions():

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Page opened: "+str(url))

    def introduce_text(self, selector, text):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, selector)
            val.clear()
            val.send_keys(text)
            print("Writing on the field {} the text -> {} ".format(selector, text))
        except TimeoutException as ex:
            print(ex.msg)
            print(selector + "Element wasn't found")

    def click_by_id(self, selector):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, selector)
            val.click()
            print("Clicking {}  ".format(selector))
        except TimeoutException as ex:
            print(ex.msg)
            print(selector + "Element wasn't found")

    def click_by_xpath(self, selector):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, selector)
            val.click()
            print("Clicking {}  ".format(selector))
        except TimeoutException as ex:
            print(ex.msg)
            print(selector + "Element wasn't found")
    def select_element_by_xpath(self, element):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, element)))
        self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, element)
        return val