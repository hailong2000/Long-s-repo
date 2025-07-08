import time
import pytest
from .base_test import BaseTest
from pages.login_page import LoginPage
import allure


@allure.feature("Đăng nhập")
class TestLoginSuccessful(BaseTest):
    @allure.story("Đăng nhập thành công")
    def test_login_successful(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username(self.config.get("username"))
        login_page.enter_password(self.config.get("password"))
        login_page.click_login_button()
        time.sleep(5)
        
        login_page.wait_for_url_contains("dashboard")
        assert "dashboard" in self.driver.current_url , "Lỗi: Không đăng nhập thành công, không tìm thấy'dashboard' trong URL"
        print("Đăng nhập thành công")