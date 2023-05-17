class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        self.driver.get(self.base_url)
