import pytest
import requests


@pytest.fixture(autouse=True, scope="class")
def setup_login(test_info):
    pass


class TestApis:
    def test_user_login(self, setup_login, test_info):
        print("\n\t\t-----Test User Login endpoint-----")
        url = 'https://gam-gam-renovacion-api.development.mag.dev/api//auth/login'
        data = {
                "username": "admin@guialemor.com",
                "password": "g4mr3n0v4c10n"
                }
        token = ''
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.post(url, data=data, headers=headers)
        try:
            assert response.status_code == 200, "ERROR. Failed to log in"
            print("Pass. Endpoint OK. ")
        except Exception as ex:
            test_info[1].append(ex)
