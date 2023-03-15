from pages.home_page import HomePage
from selenium.webdriver.common.keys import Keys
import time


class UsersPage(HomePage):

    avatar = "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']"
    cerrar_sesion = "//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root " \
                    "MuiMenuItem-gutters css-158bkwc'][contains(.,'Cerrar sesión')]"
    crear_usuario = "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]"
    confirmar_pop_up = "//button[contains(text(),'Confirmar')]"
    cancelar_pop_up = "//button[contains(text(),'Cancelar')]"
    editar = "//a[contains(text(),'{}')]//following::button[1]"
    eliminar = "//a[contains(text(),'{}')]//following::button[2]"
    deshabilitar = "//a[contains(text(),'{}')]//following::button[3]"

    def search_user(self, user):
        try:
            return self.select_element_by_xpath("//a[contains(text(),'{}')]".format(user))
        except Exception as ex:
            self.errors.append(ex.msg)
            return None

    def create_user(self):
        try:
            self.click_by_xpath(self.crear_usuario)
        except Exception as ex:
            self.errors.append(ex)

    def delete_user(self, user):
        try:
            self.click_by_xpath(self.eliminar.format(user.text))
        except Exception as ex:
            self.errors.append(ex)

    def confirm(self):
        try:
            self.click_by_xpath(self.confirmar_pop_up)
            time.sleep(2)
        except Exception as ex:
            self.errors.append(ex)

    def cancel(self):
        try:
            self.click_by_xpath(self.cancelar_pop_up)
        except Exception as ex:
            self.errors.append(ex)
