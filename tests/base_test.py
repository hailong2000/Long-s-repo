import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        config_reader = ConfigReader()
        self.config = config_reader.config
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.config.get("url"))
        self.driver.set_page_load_timeout(self.config.get("timeouts").get("page_load")) 
        print(f"The web's url is: {self.driver.current_url}")
        request.cls.driver=self.driver
        request.cls.config = self.config
        yield
        self.driver.quit()