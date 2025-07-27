import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def driver(self, request): 
        config_reader_instance = ConfigReader()
        request.cls.config = config_reader_instance.config_data 

        browser_name = request.cls.config.get("browser", "chrome") 

        if browser_name.lower() == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            _driver = webdriver.Chrome(service=service) 
        else:
            raise ValueError(f"Trình duyệt không được hỗ trợ: {browser_name}")

        _driver.maximize_window()

        base_url = request.cls.config.get("base_url") 

        if base_url:
            _driver.get(base_url)
            print(f"URL trang web là: {_driver.current_url}")
        else:
            raise ValueError("Base URL not found in testsetting.json. Please check your configuration.")

        timeouts_settings = request.cls.config.get("timeouts", {}) 
        page_load_timeout = timeouts_settings.get("page_load", 30) 
        _driver.set_page_load_timeout(page_load_timeout)

        yield _driver 
        _driver.quit()