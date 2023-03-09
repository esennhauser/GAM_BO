from pages.users_page import UsersPage
from selenium.webdriver.common.keys import Keys
import time


class NewUserPage(UsersPage):

    avatar = "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']"
    cerrar_sesion = "//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root " \
                    "MuiMenuItem-gutters css-158bkwc'][contains(.,'Cerrar sesión')]"

    nombre = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1y7uqee']//following::input[1]"
    apellido = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1y7uqee']//following::input[2]"
    user = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1y7uqee']//following::input[3]"
    email = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1y7uqee']//following::input[4]"
    password = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1y7uqee']//following::input[5]"
    habilitacion = "//body/div[@id='__next']/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]" \
                   "/label[1]/span[1]/input[1]"
    salesman = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1y7uqee']//following::input[6]"
    confirmar = "//button[contains(.,'Confirmar')]"

    # Roles
    rol = "//div[@id='select-role']"

    rol_administrador = "//body/div[@id='menu-']/div[3]/ul[1]/li[1]"
    rol_vendedor = "//body/div[@id='menu-']/div[3]/ul[1]/li[2]"
    rol_logística = "//body/div[@id='menu-']/div[3]/ul[1]/li[3]"
    rol_staff = "//body/div[@id='menu-']/div[3]/ul[1]/li[4]"
    rol_manager_gba = "//body/div[@id='menu-']/div[3]/ul[1]/li[5]"
    rol_manager_zonal = "//body/div[@id='menu-']/div[3]/ul[1]/li[6]"
    rol_ecommerce = "//body/div[@id='menu-']/div[3]/ul[1]/li[7]"
    rol_administrativo = "//body/div[@id='menu-']/div[3]/ul[1]/li[8]"
    rol_administrador_general = "//body/div[@id='menu-']/div[3]/ul[1]/li[9]"

    roles = [rol_administrador, rol_vendedor, rol_logística, rol_staff, rol_manager_gba, rol_manager_zonal,
             rol_ecommerce, rol_administrativo, rol_administrador_general]

    # Error messages
    error_nombre = "//p[contains(.,'No se permiten caracteres especiales') or contains(.,'Campo requerido')]"
    error_apellido = "//p[contains(.,'Campo requerido')]"
    error_user = "//p[contains(.,'Campo requerido')]"
    error_email = "//p[contains(.,'Debe ser un email válido')]"
    error_password = "//p[contains(.,'Campo requerido')]"
    error_rol = "//p[contains(.,'Campo requerido')]"
    error_salesman = "//p[contains(.,'Debe ingresar un número')]"

    errors = [error_nombre, error_apellido, error_user, error_email, error_password, error_rol]

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
            self.browser.select_element_by_xpath(self.rol).send_keys(Keys.TAB + Keys.SPACE)
        self.browser.select_element_by_xpath(self.rol).send_keys(Keys.TAB + Keys.TAB + salesman)
        self.browser.click_by_xpath(self.confirmar)
        time.sleep(1)

