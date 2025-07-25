import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader 

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        config_reader = ConfigReader()
        self.config = config_reader 
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        base_url = self.config.get_base_url()
        if base_url:
            self.driver.get(base_url)
        else:
        
            raise ValueError("base_url not found in testsetting.json. Please check your configuration.")
        timeouts_settings = self.config.get_timeouts()
        page_load_timeout = timeouts_settings.get("page_load", 30) 
        self.driver.set_page_load_timeout(page_load_timeout)
        print(f"URL của trang web là: {self.driver.current_url}")
        request.cls.driver = self.driver
        request.cls.config = self.config
        yield
        self.driver.quit()