import pytest
from pages.home_page import HomePage


def users_data():
    return [
        ("administrative@test.com", "g4mr3n0v4c10n"),
        ("client@test.com", "g4mr3n0v4c10n"),
        ("ecommerce@test.com", "g4mr3n0v4c10n"),
        ("general_administrator@test.com", "g4mr3n0v4c10n"),
        ("logistic@test.com", "g4mr3n0v4c10n"),
        ("manager_gba@test.com", "g4mr3n0v4c10n"),
        ("manager_zonal@test.com", "g4mr3n0v4c10n"),
        ("staff@test.com", "g4mr3n0v4c10n"),
        ("admin@guialemor.com", "g4mr3n0v4c10n")
    ]


@pytest.fixture(autouse=True, scope="class")
def setup_login(test_info):
    home_page = HomePage(test_info[0], test_info[1])
    return home_page


class TestLogOut:

    @pytest.mark.parametrize("username,password", users_data())
    def test_log_out(self, setup_login, test_info, username, password):
        print("\n\t\t-----Test log out-----")
        setup_login.login(username, password)
        inicio = setup_login.select_element_by_xpath(setup_login.mensaje_inicio)
        try:
            assert "Bienvenido" in inicio.text, "ERROR. Log in failed."
            print("Log in successful. ")
        except Exception as ex:
            test_info[1].append(ex)
        setup_login.log_out()
        welcome_message = setup_login.select_element_by_xpath(setup_login.mensaje_bienvenido)
        try:
            assert welcome_message.text == "Bienvenido a Gam", "ERROR. Log out failed."
            print("Log in and log out successful. ")
        except Exception as ex:
            test_info[1].append(ex)
