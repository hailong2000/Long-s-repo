from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    _checkout_button = (By.ID, "checkout")
    _cart_item_name = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/cart.html"

    def is_on_cart_page(self):
        """Xác minh xem trang hiện tại có phải là trang giỏ hàng hay không."""
        return self.get_current_url() == self.url

    def click_checkout_button(self):
        """Nhấp vào nút Thanh toán trên trang giỏ hàng."""
        self.click_element(self._checkout_button)
        print("Đã nhấp vào nút Thanh toán.")

    def get_items_in_cart(self):
        """Trả về danh sách tên sản phẩm hiện có trong giỏ hàng."""
        item_elements = self.find_elements(self._cart_item_name)
        return [element.text for element in item_elements]