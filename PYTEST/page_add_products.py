from Functions.functions import Functions


class FunctionsAddProducts():

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self, selector, message):
        f = Functions(self.driver)
        f.click("add-to-cart-sauce-labs-backpack")
        button = f.select_element_by_xpath(selector)
        if button.text == message:
            print("\t\t-----PASSED-----\n\n")
        else:
            print("\t\t-----FAILED-----\n\n")