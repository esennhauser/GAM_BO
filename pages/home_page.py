import time
from pages.page_login import LoginPage
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(LoginPage):

    avatar = "//*[@id='__next']/div/header/div[1]/div/div/div/span/div"
    cerrar_sesion = "(//li[@tabindex='-1'])[2]"
    mensaje_inicio = "//p[contains(.,'Bienvenido')]"
    administrador = "//p[contains(text(),'Administrador')]"
    usuarios = "(//div[contains(.,'Usuarios')])[6]"

    def log_out(self):
        try:
            self.click_by_xpath(self.avatar)
            self.click_by_xpath(self.cerrar_sesion)
            time.sleep(2)
        except Exception as ex:
            self.errors.append(ex)

    def go_to_usuarios(self):
        try:
            self.click_by_xpath(self.administrador)
            self.click_by_xpath(self.usuarios)
        except Exception as ex:
            self.errors.append(ex)