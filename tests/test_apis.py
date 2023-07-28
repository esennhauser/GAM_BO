import pytest
from pages.page_login import LoginPage
import requests


@pytest.fixture(autouse=True, scope="class")
def setup_login(test_info):
    login = LoginPage(test_info[0], test_info[1])
    return login


class TestApis:
    def test_user_login(self):
        print("\n\t\t-----Test User Login endpoint-----")
        url = 'https://gam-gam-renovacion-api.development.mag.dev/api//auth/login'
        data = {
                "username": "admin@guialemor.com",
                "password": "g4mr3n0v4c10n"
                }
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluQGd1aWFsZW1vci5jb20iLCJzdWIiOjEsInJvbGUiOiJBRE1JTiIsInR5cGUiOiJTRVNTSU9OX1RPS0VOIiwiaWF0IjoxNjg3NDYyNzI2LCJleHAiOjE2ODc0NjI3ODZ9.Oj7to_Lx8pftY67T364wjRLFtIyu4-i68PVT-Q3pEsM'
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.post(url, data=data, headers=headers)
        try:
            assert response == 200, "ERROR. Failed to log in"
            print("Pass. Endpoint OK. ")
        except Exception as ex:
            self.errors.append(ex)
