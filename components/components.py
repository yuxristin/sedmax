from selenium.webdriver.common.by import By

class WebElement:

    def __init__(self, driver, locator='', locator_type=''):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        if self.locator_type == 'name':
            return By.NAME
        if self.locator_type == 'xpath':
            return By.XPATH
        if self.locator_type == 'css':
            return By.CSS_SELECTOR
        if self.locator_type == 'class':
            return By.CLASS_NAME
        if self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('locator type ' + self.locator_type + 'not correct')
        return False


