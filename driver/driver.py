import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True, scope="class")
def driver(request):
    options = Options()
    options.headless = False
    url = "https://gam-gam-renovacion-backoffice.development.mag.dev/login"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("Page opened: " + str(url))
    return driver

