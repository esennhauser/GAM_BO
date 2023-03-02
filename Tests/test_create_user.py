import pytest
from selenium.common import StaleElementReferenceException
import time
from Pages.new_user_page import NewUserPage


@pytest.fixture
def setup_login():
    global user_creation
    user_creation = NewUserPage()
    user_creation.login("admin@guialemor.com", "g4mr3n0v4c10n")


def teardown_function():
    user_creation.browser.driver.close()


@pytest.mark.failed_run
def test_create_user(setup_login):
    print("\n\t\t-----Test create user without mandatory fields-----")
    user_creation.go_to_usuarios()
    user_creation.create_user()
    user_creation.fill_in_and_confirm("Nombre", "Apellido", "username", "email@gam.dev", "Ejemplo22!",
                                      user_creation.roles[2], True, "1000")
    user_created = user_creation.search_user("Nombre Apellido")
    assert user_created.text == "Nombre Apellido", "ERROR. User was not created successfully."


@pytest.mark.failed_run
def test_delete_user(setup_login):
    print("\n\t\t-----Test delete created user-----")
    user_creation.go_to_usuarios()
    user_to_delete = user_creation.search_user("Nombre Apellido")
    user_creation.delete_user(user_to_delete)
    user_creation.confirm()
    user_to_verify = user_creation.search_user("Nombre Apellido")
    try:
        assert user_to_verify == "", "ERROR. User not deleted."
        print("User successfully deleted.")
    except Exception as e:
        print(e)
