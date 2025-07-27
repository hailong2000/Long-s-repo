import pytest
import allure
from pages.login_page import LoginPage
from base.base_test import BaseTest

@allure.feature("Kiểm tra đăng nhập thành công!")
class TestLogin(BaseTest): 

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver): 
        self.login_page = LoginPage(driver)

    @allure.story("Đăng nhập với thông tin đúng")
    @allure.description("Kiểm thử để xác minh rằng người dùng đăng nhập bằng thông tin đăng nhập đúng.")
    def test_valid_login(self): 
        username = self.config.get("credentials").get("username")
        password = self.config.get("credentials").get("password")

        self.login_page.open_page()
        self.login_page.login(username, password)

        self.login_page.wait_for_url_contains("inventory.html")

        assert self.login_page.wait_for_url_contains("inventory.html"), "Đăng nhập thất bại hoặc URL không chuyển đến trang sản phẩm."
        print("Đăng nhập thành công!")