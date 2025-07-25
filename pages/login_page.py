from selenium.webdriver.common.by import By
from base.base_page import BasePage 

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.XPATH, "//input[@type='text']")
        self.password_field = (By.XPATH, "//input[@type='password']")
        self.login_button = (By.XPATH, "//input[@type='submit']")

    def enter_username(self, username):
        username_element = self.wait_for_element_to_be_clickable(self.username_field)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.wait_for_element_to_be_clickable(self.password_field)
        password_element.clear()
        password_element.send_keys(password)

    def click_login_button(self):
        login_button_element = self.wait_for_element_to_be_clickable(self.login_button)
        login_button_element.click()
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_url_contains("inventory.html")
        
 