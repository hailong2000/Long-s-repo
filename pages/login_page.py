from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    username_input =(By.NAME ,"username")
    password_input =(By.NAME ,"password")
    login_btn=(By.XPATH ,"//button[@type='submit']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def enter_username(self , username):
        username_filed = self.wait_for_element_to_be_clickable(self.username_input)
        username_filed.send_keys(username)
        print("Đã nhập username")
    
    def enter_password(self, password):
        password_field = self.wait_for_element_to_be_clickable(self.password_input)
        password_field.send_keys(password)
        print("Đã nhập password")
        
    def click_login_button(self):
        login_button = self.wait_for_element_to_be_clickable(self.login_btn)
        login_button.click()