import time
from pages.demo_sedmax import DemoSedMax
from components.components import WebElement

def test_login_form(browser):
    form = DemoSedMax(browser)
    form.visit()

    form.btn_v.click()

