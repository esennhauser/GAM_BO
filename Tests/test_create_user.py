import pytest
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
    user_creation.fill_in_and_confirm("Nombre", "Apellido", "username", "email@gam.dev", "Ejemplo22!", "Logística",
                                      True, "1000")
    user_created = user_creation.browser.driver.find_element(By.LINK_TEXT, "Nombre Apellido")
    assert user_created.text == "Nombre Apellido"
