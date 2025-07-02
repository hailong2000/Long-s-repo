import time
from .base_test import BaseTest
from pages.login_page import LoginPage

class TestLoginSuccess(BaseTest):
    def test_login_successful(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
        time.sleep(5)
        login_page.wait_for_url_contains("dashboard")
        assert "dashboard" in self.driver.current_url ,"ERROR: Không đăng nhập thành công!!!"
        print("Đăng nhập thành công!")