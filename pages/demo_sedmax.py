

class DemoSedMax:

        def __init__(self, driver):
            self.base_url = 'https://demo.sedmax.ru/'
            super().__init__(driver, self.base_url)
            self.text_element = WebElement(driver, 'section1Content > p')
