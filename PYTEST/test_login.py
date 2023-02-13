from PYTEST.Pages.page_login import FunctionsLogin

def test_failed_logins():
    driver = ""
    print("\n\t\t-----Test wrong username and wrong password-----")
    login_function = FunctionsLogin(driver)
    login_function.failed_login("ernesto", "password123", "Email or Password is invalid")
    login_function.f.driver.close()

    print("\t\t-----Test empty username and empty password-----")
    login_function = FunctionsLogin(driver)
    login_function.failed_login("", "", "username must be at least 6 characters")
    login_function.f.driver.close()

    print("\t\t-----Test wrong password-----")
    login_function = FunctionsLogin(driver)
    login_function.failed_login("standard_user", "password123", "Email or Password is invalid")
    login_function.f.driver.close()
def test_successful_logins():
    driver = ""
    print("\t\t-----Test standard_user login-----")
    login_function = FunctionsLogin(driver)
    login_function.successful_login("test_1", "Magnetico22!", "Inicio")
    login_function.f.driver.close()

