from pages.base_page import BasePage
from components.components import WebElement
class DemoSedMax(BasePage):

        def __init__(self, driver):
            self.driver = driver
            self.base_url = 'https://demo.sedmax.ru/'
            super().__init__(driver, self.base_url)
            self.login = WebElement(driver, '#Login')
            self.password = WebElement(driver, '#Password')
            self.btn_v = WebElement(driver, '#main > div > div > form > button')
            self.alert_message = WebElement(driver, '#main > div > div > form > div.ant-login-alert.ant-login-alert-error.ant-login-alert-no-icon.login-login-form-module_error___Fq9km > div > div')
            self.visible_pass = WebElement(driver, '#main > div > div > form > div:nth-child(2) > div > div > div > div > span > span.ant-login-input-suffix > span > svg')




