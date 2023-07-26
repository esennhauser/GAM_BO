import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pages.google_login_page import GoogleLoginPage


@pytest.fixture(scope="class")
def driver(request):
    gam_dev = "https://gam-gam-renovacion-backoffice.development.mag.dev/login"

    options = ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Axel\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 8")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    errors = []
    driver.get(gam_dev)
    driver.implicitly_wait(10)

    print("Page opened: " + str(gam_dev))

    request.node.errors = errors
    request.node.driver = driver
    yield

    # Printing errors
    errors_verified = errors.copy()
    for e in errors:
        if e == "":
            errors_verified.remove(e)
        else:
            pass
    if len(errors_verified) == 0:
        print("\n\t\tTest finished with no errors. ")
    else:
        print(errors_verified)

    driver.quit()
    print("\n\t\tTest is finished.")
