import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException 

class TestCheckoutScenario(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.driver = driver     
        self.wait = WebDriverWait(driver, 10)
       
       

    def test_add_3_products_and_complete_checkout(self):
        
        username = self.config.get("credentials").get("username")
        password = self.config.get("credentials").get("password")
        
        self.login_page.open_page()
        self.login_page.login(username, password)
        
        print(f"Current URL after login attempt: {self.driver.current_url}")
        assert self.inventory_page.is_on_inventory_page(), "Không ở trên trang sản phẩm sau khi đăng nhập."

        
        products_added = self.inventory_page.add_multiple_products_to_cart(num_products=3)
        assert len(products_added) == 3, f"Dự kiến 3 sản phẩm được thêm, nhưng đã thêm {len(products_added)} sản phẩm."
        print(f"Đã thêm các sản phẩm sau vào giỏ hàng: {products_added}")

        
        self.inventory_page.click_shopping_cart_icon()
        assert self.cart_page.is_on_cart_page(), "Không ở trên trang giỏ hàng sau khi nhấp vào biểu tượng giỏ hàng."
        
        self.cart_page.click_checkout_button()
        
     
        try:
            self.wait.until(EC.presence_of_element_located(self.checkout_page._first_name_field))
            print(f"DEBUG: Đã chờ thành công trường First Name trên trang Checkout Step One.")
        except TimeoutException:
            print(f"LỖI: Không thể tìm thấy trường First Name trên trang Checkout Step One trong thời gian chờ.")
            print(f"DEBUG: Current URL at checkout step one timeout: {self.driver.current_url}")
            self.driver.save_screenshot("debug_checkout_step_one_timeout.png") 
            raise 

        print(f"DEBUG: URL sau khi nhấp Checkout: {self.driver.current_url}") 
        assert self.driver.current_url == self.checkout_page.url_step_one, "Không ở trên trang bước một của thanh toán."

        
        first_name = "John"
        last_name = "Doe"
        zip_code = "70000"
        self.checkout_page.enter_shipping_information(first_name, last_name, zip_code)

        self.checkout_page.click_continue_button()
        
       
        try:
            self.wait.until(EC.presence_of_element_located(self.checkout_page._finish_button))
            print(f"DEBUG: Đã chờ thành công nút Finish trên trang Checkout Step Two.")
        except TimeoutException:
            print(f"LỖI: Không thể tìm thấy nút Finish trên trang Checkout Step Two trong thời gian chờ.")
            print(f"DEBUG: Current URL at checkout step two timeout: {self.driver.current_url}")
            self.driver.save_screenshot("debug_checkout_step_two_timeout.png")
            raise 
        
        assert self.driver.current_url == self.checkout_page.url_step_two, "Không ở trên trang bước hai của thanh toán."
        
        self.checkout_page.click_finish_button()
        
     
        try:
            self.wait.until(EC.presence_of_element_located(self.checkout_page._thank_you_header))
            print(f"DEBUG: Đã chờ thành công tiêu đề xác nhận trên trang Checkout Complete.")
        except TimeoutException:
            print(f"LỖI: Không thể tìm thấy tiêu đề xác nhận trên trang Checkout Complete trong thời gian chờ.")
            print(f"DEBUG: Current URL at checkout complete timeout: {self.driver.current_url}")
            self.driver.save_screenshot("debug_checkout_complete_timeout.png")
            raise 
        
        assert self.checkout_page.is_on_checkout_complete_page(), "Không ở trên trang hoàn tất thanh toán."

        
        expected_header = "Thank you for your order!"
        expected_text = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

        actual_header = self.checkout_page.get_confirmation_header()
        actual_text = self.checkout_page.get_confirmation_text()

        assert actual_header == expected_header, \
            f"Tiêu đề xác nhận không khớp. Dự kiến: '{expected_header}', Thực tế: '{actual_header}'"
        assert actual_text == expected_text, \
            f"Văn bản xác nhận không khớp. Dự kiến: '{expected_text}', Thực tế: '{actual_text}'"
        print("Các thông báo xác nhận đơn hàng đã được xác minh thành công!")