from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_locator =(By.NAME , "username")
        self.password_locator=(By.NAME ,"password")
        self.login_button_locator=(By.XPATH,"//button[@type='submit']")
    
    def enter_username(self , username):
        username_textbox = self.wait_for_element_to_be_clickable(self.username_locator)
        username_textbox.send_keys(username)
        print("Đã nhập username")
        
    def enter_password(self, password):
        password_textbox = self.wait_for_element_to_be_clickable(self.password_locator)
        password_textbox.send_keys(password)
        print("Đã nhập password")
        
    def click_login_button(self):
        login_button = self.wait_for_element_to_be_clickable(self.login_button_locator)
        login_button.click()
        print("Đã nhấn nút Login")