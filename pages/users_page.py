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
        except Exception as e:
            print("Unable to find user.")
            return None

    def create_user(self):
        self.click_by_xpath(self.crear_usuario)

    def delete_user(self, user):
        self.click_by_xpath(self.eliminar.format(user.text))

    def confirm(self):
        self.click_by_xpath(self.confirmar_pop_up)
        time.sleep(2)

    def cancel(self):
        self.click_by_xpath(self.cancelar_pop_up)
