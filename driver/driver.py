import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage


@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.headless = False
    url = "https://gam-gam-renovacion-backoffice.development.mag.dev/login"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("Page opened: " + str(url))
    errors = []
    request.cls.errors = errors
    request.cls.driver = driver
    yield
    print(errors)
    driver.close()
    driver.quit()
    print("Test is finished.")
