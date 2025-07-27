from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    _username_field = (By.XPATH, "//input[@type='text']")
    _password_field = (By.XPATH, "//input[@type='password']")
    _login_button = (By.XPATH, "//input[@type='submit']")
    _error_message = (By.CSS_SELECTOR, "[data-test='error']") 

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/" 

    def open_page(self):
        """Mở trực tiếp trang đăng nhập Sauce Demo."""
        self.open_url(self.url)
        print("Đã mở trang đăng nhập.")

    def enter_username(self, username):
        """Nhập tên người dùng vào trường tên người dùng."""
        self.send_keys(self._username_field, username) 

    def enter_password(self, password):
        """Nhập mật khẩu vào trường mật khẩu."""
        self.send_keys(self._password_field, password) 

    def click_login_button(self):
        """Nhấp vào nút đăng nhập."""
        self.click_element(self._login_button) 

    def login(self, username, password):
        """Thực hiện hành động đăng nhập với thông tin đăng nhập đã cho."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        print(f"Đã cố gắng đăng nhập với tên người dùng: {username}")


    def get_error_message(self):
        """Trả về văn bản của thông báo lỗi, nếu có."""
        try:
            return self.get_element_text(self._error_message)
        except Exception:
            return None 