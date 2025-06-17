import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
        self.driver.set_page_load_timeout(45) 
        print(f"The web's url is: {self.driver.current_url}")
        request.cls.driver=self.driver
        yield
        self.driver.quit()
   

class TestSuccessfulLogin(BaseTest):
    def test_successful_login(self):
        username_textbox= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
        username_textbox.send_keys("Admin")
        print("[Test 2] Đã nhập tên người dùng.")

        password_textbox= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password_textbox.send_keys("admin123")
        print("[Test 2] Đã nhập mật khẩu.")

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()
        
        print("[Test 2] Đã nhấp nút Đăng nhập.")
        time.sleep(5)
        
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("dashboard")
        )
        current_url_after_login = self.driver.current_url
        print(f"[Test 2] URL hiện tại sau đăng nhập: '{current_url_after_login}'")
        assert "dashboard" in current_url_after_login, \
        f"Lỗi: Đăng nhập không thành công. URL không chứa 'dashboard'. URL thực tế: {current_url_after_login}"
    
        print("[Test 2] Đăng nhập thành công: PASSED.")