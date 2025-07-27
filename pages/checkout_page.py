# pages/checkout_page.py

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    _first_name_field = (By.ID, "first-name")
    _last_name_field = (By.ID, "last-name")
    _zip_postal_code_field = (By.ID, "postal-code")
    _continue_button = (By.ID, "continue")
    _finish_button = (By.ID, "finish")
    _thank_you_header = (By.CLASS_NAME, "complete-header")
    _order_dispatched_text = (By.CLASS_NAME, "complete-text")

    def __init__(self, driver):
        super().__init__(driver)
        self.url_step_one = "https://www.saucedemo.com/checkout-step-one.html"
        self.url_step_two = "https://www.saucedemo.com/checkout-step-two.html"
        self.url_complete = "https://www.saucedemo.com/checkout-complete.html"

    def enter_shipping_information(self, first_name, last_name, zip_code):
        """Nhập thông tin vận chuyển vào trang bước một của thanh toán."""
        self.send_keys(self._first_name_field, first_name)
        self.send_keys(self._last_name_field, last_name)
        self.send_keys(self._zip_postal_code_field, zip_code)
        print(f"Đã nhập thông tin vận chuyển: {first_name} {last_name}, {zip_code}")

    def click_continue_button(self):
        """Nhấp vào nút Tiếp tục trên bước một của thanh toán."""
        self.click_element(self._continue_button)
        print("Đã nhấp vào nút Tiếp tục.")

    def click_finish_button(self):
        """Nhấp vào nút Hoàn tất trên bước hai của thanh toán."""
        self.click_element(self._finish_button)
        print("Đã nhấp vào nút Hoàn tất.")

    def get_confirmation_header(self):
        """Trả về văn bản của tiêu đề xác nhận."""
        return self.get_element_text(self._thank_you_header)

    def get_confirmation_text(self):
        """Trả về văn bản của thông báo đơn hàng đã được gửi đi."""
        return self.get_element_text(self._order_dispatched_text)

    def is_on_checkout_complete_page(self):
        """Xác minh xem trang hiện tại có phải là trang hoàn tất thanh toán hay không."""
        return self.get_current_url() == self.url_complete