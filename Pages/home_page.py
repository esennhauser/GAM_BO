import time
from Pages.page_login import LoginPage
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(LoginPage):

    avatar = "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-yq2ef9']"
    cerrar_sesion = "(//li[@tabindex='-1'])[2]"
    mensaje_inicio = "//h6[contains(.,'Gam')]"
    administrador = "//p[contains(text(),'Administrador')]"
    usuarios = "//header/div[2]/div[1]/div[1]/div[8]/div[1]/div[1]/div[1]/a[4]/div[1]"

    def log_out(self):
        self.browser.click_by_xpath(self.avatar)
        self.browser.click_by_xpath(self.cerrar_sesion)
        time.sleep(1)

    def go_to_usuarios(self):
        action = ActionChains(self.driver)
        administrador = self.select_element_by_xpath(self.administrador)
        action.move_to_element(administrador).perform()
        usuarios = self.select_element_by_xpath(self.usuarios)
        action.move_to_element(usuarios)
        action.click(usuarios).perform()
