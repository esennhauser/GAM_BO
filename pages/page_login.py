import time
from pages.base_page import BasePage



class LoginPage(BasePage):

    username_textbox ="//input[contains(@type,'text')]"
    password_textbox = "//input[@id='auth-login-password']"
    login_button ="//*[@id='__next']/div/div/div/div/div/form/button"
    username_error = "//*[@id='__next']/div/div/div/div/div/form/div[1]/p"
    password_error = "//p[@id='']"
    mensaje_bienvenido = "//h5[contains(.,'Bienvenido a Gam')]"

    def login(self, username, password):
        try:
            self.introduce_text_by_xpath(self.username_textbox, username)
            self.introduce_text_by_xpath(self.password_textbox, password)
            self.click_by_xpath(self.login_button)
            time.sleep(3)
        except Exception as ex:
            self.errors.append(ex)

