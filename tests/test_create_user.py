import pytest
from pages.new_user_page import NewUserPage


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


@pytest.fixture(scope="class", autouse=True)
def setup_login(test_info):
    new_user = NewUserPage(test_info[0], test_info[1])
    new_user.login("admin@guialemor.com", "g4mr3n0v4c10n")
    new_user.go_to_usuarios()
    new_user.create_user()
    return new_user


class TestFailedUserCreation:

    def test_failed_user_creation(self, setup_login, test_info):
        print("\n\t\t-----Test create user with invalid email field. -----")
        setup_login.fill_in_and_confirm("Automated01", "Test", "automated01",
         "automated01gmail", "Password123", NewUserPage.rol_logística, True, "")
        error_message = setup_login.select_element_by_xpath(setup_login.error_email)
        try:
            assert error_message.text == "Debe ser un email válido", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)
        setup_login.go_to_usuarios()
        print("\n\t\t-----Test create user with a mandatory empty field. -----")
        setup_login.create_user()
        setup_login.fill_in_and_confirm("Automated02", "", "automated02",
         "automated02@gmail.com", "Password123", NewUserPage.rol_staff, True, "1")
        error_message = setup_login.select_element_by_xpath(setup_login.error_apellido)
        try:
            assert error_message.text == "Campo requerido", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)
        setup_login.go_to_usuarios()
        print("\n\t\t-----Test create seller user with the salesman field empty. -----")
        setup_login.create_user()
        setup_login.fill_in_and_confirm("Automated03", "Test", "automated03",
         "automated03@gmail.com", "Password123", NewUserPage.rol_vendedor, False, "")
        error_message = setup_login.select_element_by_xpath(setup_login.error_salesman)
        try:
            assert error_message.text == "Debe ingresar un número", "ERROR. Unexpected error message."
            print("Error message as expected. ")
        except Exception as ex:
            test_info[1].append(ex)


class TestSuccessfulUserCreation:
    @pytest.mark.parametrize("nombre_test,nombre,apellido,username,email,contra,rol,habilitado,salesman",
                             successful_creation_user_data(), scope="class")
    def test_successful_user_creation(self, setup_login, test_info, nombre_test, nombre, apellido, username, email, contra, rol,
                                      habilitado, salesman):
        print("\n\t\t-----Test {}-----".format(nombre_test))
        setup_login.fill_in_and_confirm(nombre, apellido, username, email, contra,
                                          rol, habilitado, salesman)
        user_created = setup_login.search_user(nombre + " " + apellido)
        try:
            assert user_created.text == (nombre + " " + apellido), "ERROR. User was not created successfully."
            print("User successfully created.")
        except Exception as ex:
            test_info[1].append(ex)

    @pytest.mark.parametrize("nombre_test,nombre,apellido,username,email,contra,rol,habilitado,salesman",
                             successful_creation_user_data(), scope="class")
    def test_delete_user(self, setup_login, test_info, nombre_test, nombre, apellido, username, email, contra, rol, habilitado, salesman):
        print("\n\t\t-----Test delete created user-----")
        user_to_delete = setup_login.search_user(nombre + " " + apellido)
        setup_login.delete_user(user_to_delete)
        setup_login.confirm()
        user_to_verify = setup_login.search_user(nombre + " " + apellido)
        try:
            assert user_to_verify == None, "ERROR. User not deleted."
            print("User successfully deleted.")
        except Exception as ex:
            test_info[1].append(ex)
        setup_login.go_to_usuarios()
        setup_login.create_user()
