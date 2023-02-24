from Pages.users_page import UsersPage


class NewUserPage(UsersPage):
    avatar = "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']"
    cerrar_sesion = "//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root " \
                    "MuiMenuItem-gutters css-158bkwc'][contains(.,'Cerrar sesión')]"
    nombre = "//input[@id=':rf:']"
    apellido = "//input[@id=':rg:']"
    user = "//input[@id=':rh:']"
    email = "//input[@id=':ri:']"
    password = "//input[@id=':rj:']"
    rol = "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[6]/div[1]/fieldset[1]"
    habilitacion = "//body/div[@id='__next']/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/label[1]/span[1]/input[1]"
    salesman = "//input[@id=':r32:']"
    confirmar = "//body/div[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[9]/button[1]"

    def fill_in_and_confirm(self, nombre, apellido, user, email, password, rol, habilitacion, salesman):
        self.introduce_text_by_xpath(self.nombre, nombre)
        self.introduce_text_by_xpath(self.apellido, apellido)
        self.introduce_text_by_xpath(self.user, user)
        self.introduce_text_by_xpath(self.email, email)
        self.introduce_text_by_xpath(self.password, password)
        self.browser.select_option_by_xpath(self.rol, rol)
        if habilitacion is True:
            pass
        else:
            self.browser.click_by_xpath(self.habilitacion)
        self.browser.introduce_text_by_xpath(self.salesman, salesman)
        self.browser.click_by_xpath(self.confirmar)

