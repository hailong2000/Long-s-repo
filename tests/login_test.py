from pages.login_page import LoginPage
from base.base_test import BaseTest   
import allure
import time

@allure.feature("Login Tests")
class TestLogin(BaseTest):
    @allure.story("Valid Login")
    @allure.description("Test to verify that a user can log in with valid credentials.")
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        credentials_data = self.config.get_credentials()
        username = credentials_data.get("username")
        password = credentials_data.get("password")
        login_page.login(username, password)
        time.sleep(2)   # Wait for the page to load completely  
        assert "inventory.html" in self.driver.current_url, "Login failed or URL did not change to inventory page."
        print("Successfully logged in ")