import time

from pages.demo_sedmax import DemoSedMax
from components.components import WebElement

def test_login_form(browser):
    form = DemoSedMax(browser)
    form.visit()

    time.sleep(4)
    form.login.send_keys('Unregistered')
    form.password.send_keys('User')
    time.sleep(2)
    form.btn_v.click()
    time.sleep(2)
    form.visible_pass.click()
    time.sleep(2)
    assert form.alert_message.get_text() == 'Неверные логин или пароль'
