import time
from pages.base_page import BasePage


class GoogleLoginPage(BasePage):

    username_textbox = "//*[@id='identifierId']"
    password_textbox = "//*[@id='password']/div[1]/div/div[1]/input"
    next_button_identifier = "//*[@id='identifierNext']/div/button/span"
    next_button_password = "//*[@id='passwordNext']/div/button/span"

    def login(self, username, password):
        try:
            self.introduce_text_by_xpath(self.username_textbox, username)
            self.click_by_xpath(self.next_button_identifier)
            time.sleep(4)
            self.introduce_text_by_xpath(self.password_textbox, password)
            self.click_by_xpath(self.next_button_password)
            time.sleep(4)
        except Exception as ex:
            self.errors.append(ex)
