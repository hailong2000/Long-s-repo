from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        
    def wait_for_element_to_be_clickable(self, locator, timeout =10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        
    def wait_for_url_contains(self, url_check ,timeout =10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_check)
        )