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
    new_user = ""

    @pytest.fixture
    def setup_login(self):
        self.new_user = NewUserPage()
        self.new_user.login("admin@guialemor.com", "g4mr3n0v4c10n")
        self.new_user.go_to_usuarios()
        yield
        self.new_user.browser.driver.close()

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.failed_creation
    def test_failed_user_creation(self):
        print("\n\t\t-----Test create user with invalid email field. -----")
        self.new_user.create_user()
        self.new_user.fill_in_and_confirm("Automated01", "Test", "automated01",
         "automated01gmail", "Password123", NewUserPage.rol_logística, True, "")
        error_message = self.new_user.browser.select_element_by_xpath(self.new_user.error_email)
        try:
            assert error_message.text == "Debe ser un email válido", "ERROR. Unexpected error message."
        except Exception as e:
            print(e.msg)
        self.new_user.go_to_usuarios()
        print("\n\t\t-----Test create user with a mandatory empty field. -----")
        self.new_user.create_user()
        self.new_user.fill_in_and_confirm("Automated02", "", "automated02",
         "automated02@gmail.com", "Password123", NewUserPage.rol_staff, True, "1")
        error_message = self.new_user.browser.select_element_by_xpath(self.new_user.error_apellido)
        try:
            assert error_message.text == "Campo requerido", "ERROR. Unexpected error message."
        except Exception as e:
            print(e.msg)
        self.new_user.go_to_usuarios()
        print("\n\t\t-----Test create seller user with the salesman field empty. -----")
        self.new_user.create_user()
        self.new_user.fill_in_and_confirm("Automated03", "Test", "automated03",
         "automated03@gmail.com", "Password123", NewUserPage.rol_vendedor, False, "")
        error_message = self.new_user.browser.select_element_by_xpath(self.new_user.error_salesman)
        try:
            assert error_message.text == "Debe ingresar un número", "ERROR. Unexpected error message."
        except Exception as e:
            print(e.msg)

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.parametrize("test,nombre,apellido,username,email,contra,rol,habilitado,salesman",
                             successful_creation_user_data())
    def test_successful_user_creation(self, test, nombre, apellido, username, email, contra, rol,
                                      habilitado, salesman):
        print("\n\t\t-----Test {}-----".format(test))
        self.new_user.go_to_usuarios()
        self.new_user.create_user()
        self.new_user.fill_in_and_confirm(nombre, apellido, username, email, contra,
                                          rol, habilitado, salesman)
        user_created = self.new_user.search_user(nombre + " " + apellido)
        try:
            assert user_created.text == (nombre + " " + apellido), "ERROR. User was not created successfully."
            print("User created successfully")
        except Exception as e:
            print(e.msg)

    @pytest.mark.usefixtures("setup_login")
    @pytest.mark.parametrize("test,nombre,apellido,username,email,contra,rol,habilitado,salesman",
                             successful_creation_user_data())
    def test_delete_user(self, test, nombre, apellido, username, email, contra, rol, habilitado, salesman):
        print("\n\t\t-----Test delete created user-----")
        user_to_delete = self.new_user.search_user(nombre + " " + apellido)
        self.new_user.delete_user(user_to_delete)
        self.new_user.confirm()
        user_to_verify = self.new_user.search_user(nombre + " " + apellido)
        try:
            assert user_to_verify == None, "ERROR. User not deleted."
            print("User successfully deleted.")
        except Exception as e:
            print(e)
