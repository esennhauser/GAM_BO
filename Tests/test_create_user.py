import pytest
from selenium.common import StaleElementReferenceException
import time
from Pages.new_user_page import NewUserPage


def successful_creation_user_data():
    return [
        ("create user with only mandatory fields.", "Automated01", "Test", "automated01",
         "automated01@gmail.com", "Password123", NewUserPage.roles[2], True, ""),
        ("create user with mandatory and not mandatory fields.", "Automated02", "Test", "automated02",
         "automated02@gmail.com", "Password123", NewUserPage.roles[0], True, "1"),
        ("create disabled user.", "Automated03", "Test", "automated03", "automated03@gmail.com",
         "Password123", NewUserPage.roles[3], False, "2"),
        ("create seller user with additional fields.", "Automated04", "Test", "automated04",
         "automated04@gmail.com", "Password123", NewUserPage.roles[4], True, "3")
    ]


class TestCreateUser:

    @pytest.fixture(scope="class")
    def setup_login(self):
        global user_creation
        user_creation = NewUserPage()
        user_creation.login("admin@guialemor.com", "g4mr3n0v4c10n")
        user_creation.go_to_usuarios()

    def teardown_function(self):
        user_creation.browser.driver.close()

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.failed_creation
    def test_failed_user_creation(self):
        print("\n\t\t-----Test create user with invalid email field. -----")
        user_creation.create_user()
        user_creation.fill_in_and_confirm("Automated01", "Test", "automated01",
         "automated01gmail", "Password123", NewUserPage.rol_logística, True, "")
        error_message = user_creation.browser.select_element_by_xpath(user_creation.error_email)
        assert error_message.text == "Debe ser un email válido", "ERROR. Unexpected error message."
        user_creation.go_to_usuarios()
        print("\n\t\t-----Test create user with a mandatory empty field. -----")
        user_creation.create_user()
        user_creation.fill_in_and_confirm("Automated02", "", "automated02",
         "automated02@gmail.com", "Password123", NewUserPage.rol_staff, True, "1")
        error_message = user_creation.browser.select_element_by_xpath(user_creation.error_apellido)
        assert error_message.text == "Campo requerido", "ERROR. Unexpected error message."
        user_creation.go_to_usuarios()
        print("\n\t\t-----Test create seller user with the salesman field empty. -----")
        user_creation.create_user()
        user_creation.fill_in_and_confirm("Automated03", "Test", "automated03",
         "automated03@gmail.com", "Password123", NewUserPage.rol_vendedor, False, "")
        error_message = user_creation.browser.select_element_by_xpath(user_creation.error_salesman)
        assert error_message.text == "Debe ingresar un número", "ERROR. Unexpected error message."

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.successful_creation
    @pytest.mark.parametrize("test,nombre,apellido,username,email,contra,rol,habilitado,salesman",
                             successful_creation_user_data(), scope="class")
    def test_successful_user_creation(self, test, nombre, apellido, username, email, contra, rol,
                                      habilitado, salesman):
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
    @pytest.mark.parametrize("test,nombre,apellido,username,email,contra,rol,habilitado,salesman",
                             successful_creation_user_data(), scope="class")
    def test_delete_user(self, test, nombre, apellido, username, email, contra, rol, habilitado, salesman):
        print("\n\t\t-----Test delete created user-----")
        user_to_delete = user_creation.search_user(nombre + " " + apellido)
        user_creation.delete_user(user_to_delete)
        user_creation.confirm()
        user_to_verify = user_creation.search_user(nombre + " " + apellido)
        try:
            assert user_to_verify == "", "ERROR. User not deleted."
            print("User successfully deleted.")
        except Exception as e:
            print(e)
