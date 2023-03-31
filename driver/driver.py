import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pages.google_login_page import GoogleLoginPage


@pytest.fixture(scope="class")
def driver(request):
    google = "https://accounts.google.com/signin"
    gam_dev = "https://gam-gam-renovacion-backoffice.development.mag.dev/login"
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    errors = []
    driver.get(google)
    # Loading cookies
    try:
        with open("cookies.txt", "r") as f:
            cookies = eval(f.read())
        for cookie in cookies:
            driver.add_cookie({cookie})
    except Exception as ex:
        print("No cookies loaded. ")
        google_login = GoogleLoginPage(driver, errors)
        google_login.login("ernesto@magnetico.dev", "Elquedepositodolares2003")
        # Saving cookies
        cookies = driver.get_cookies()
        with open("cookies.txt", "w") as f:
            f.write(str(cookies))

    driver.get(gam_dev)
    driver.implicitly_wait(10)

    print("Page opened: " + str(gam_dev))

    request.cls.errors = errors
    request.cls.driver = driver
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



    driver.close()
    print("\n\t\tTest is finished.")
