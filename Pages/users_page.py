from Pages.home_page import HomePage


class UsersPage(HomePage):
    avatar = "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']"
    cerrar_sesion = "//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root " \
                    "MuiMenuItem-gutters css-158bkwc'][contains(.,'Cerrar sesión')]"
    crear_usuario = "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]"

    def create_user(self):
        self.browser.click_by_xpath(self.crear_usuario)
