import pytest
from selenium.common import StaleElementReferenceException
import time
from Pages.new_user_page import NewUserPage


def users_data():
    return [
        ("create user with only mandatory fields.", "Jorge Luis", "Borges", "jorgeluisborges",
         "jorgeluisborges@gmail.com", "Contrasena123", NewUserPage.roles[2], True, ""),
        ("create user with mandatory and not mandatory fields.", "Juan", "Pérez", "juanperez", "juanperez@gmail.com",
         "Contrasena123", NewUserPage.roles[0], True, "1"),
        ("create disabled user.", "Moria", "Casan", "moriacasan", "moriacasan@gmail.com",
         "Contrasena123", NewUserPage.roles[3], False, "2"),
        ("create seller user with additional fields.", "Lobo", "Dewallstreet", "lobodewallstreet",
         "lobodewallstreet@gmail.com", "Contrasena123", NewUserPage.roles[4], True, "3")
    ]


class TestCreateUser:
    @pytest.fixture(scope="class")
    def setup_login(self):
        global user_creation
        user_creation = NewUserPage()
        user_creation.login("admin@guialemor.com", "g4mr3n0v4c10n")

    def teardown_function(self):
        user_creation.browser.driver.close()

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.create
    @pytest.mark.parametrize("test,nombre,apellido,username,email,contra,rol,habilitado,salesman", users_data(),
                             scope="class")
    def test_create_user(self, test, nombre, apellido, username, email, contra, rol, habilitado, salesman):
        print("\n\t\t-----Test {}-----".format(test))
        user_creation.go_to_usuarios()
        user_creation.create_user()
        user_creation.fill_in_and_confirm(nombre, apellido, username, email, contra,
                                          rol, habilitado, salesman)
        user_created = user_creation.search_user(nombre + " " + apellido)
        try:
            assert user_created.text == (nombre + " " + apellido), "ERROR. User was not created successfully."
        except Exception as e:
            print(e)

    @pytest.mark.delete
    @pytest.mark.parametrize("test,nombre,apellido,username,email,contra,rol,habilitado,salesman", users_data(),
                             scope="class")
    def test_delete_user(self, test, nombre, apellido, username, email, contra, rol, habilitado, salesman):
        print("\n\t\t-----Test delete created user-----")
        user_creation.go_to_usuarios()
        user_to_delete = user_creation.search_user(nombre + " " + apellido)
        user_creation.delete_user(user_to_delete)
        user_creation.confirm()
        user_to_verify = user_creation.search_user(nombre + " " + apellido)
        try:
            assert user_to_verify == "", "ERROR. User not deleted."
            print("User successfully deleted.")
        except Exception as e:
            print(e)
