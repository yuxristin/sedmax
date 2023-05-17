from selenium.webdriver.common.by import By
class WbElement:

    def __init__(self, driver, locator='', locator_type = 'css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def click(self):
        self.find_element().click()

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