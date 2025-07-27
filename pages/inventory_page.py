from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    _add_to_cart_button_id_template = "add-to-cart-{}" 
    _shopping_cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")
    _product_names = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/inventory.html"

    def is_on_inventory_page(self):
        return self.get_current_url() == self.url

    def add_product_to_cart(self, product_name):
        if "Test.allTheThings() T-Shirt (Red)" == product_name:
             formatted_product_name = "test.allthethings()-t-shirt-(red)"
        else:
            formatted_product_name = product_name.lower().replace(' ', '-')
        
        locator = (By.ID, self._add_to_cart_button_id_template.format(formatted_product_name))

        try:
            print(f"DEBUG: Đang cố gắng thêm '{product_name}' sử dụng locator: {locator}")
            self.wait.until(EC.visibility_of_element_located(locator)) 
            self.click_element(locator) 
            print(f"Đã thêm '{product_name}' vào giỏ hàng.")
            
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException) as e:
            
            print(f"LỖI: Không thể tìm thấy hoặc nhấp vào nút 'Add to Cart' cho '{product_name}' với locator {locator}.")
            print(f"Chi tiết lỗi: {e}")
            try:
                self.driver.save_screenshot(f"debug_add_to_cart_error_{product_name.replace(' ', '_').lower()}.png") 
                print(f"Đã lưu ảnh màn hình lỗi tại: debug_add_to_cart_error_{product_name.replace(' ', '_').lower()}.png")
            except Exception as screenshot_e:
                print(f"CẢNH BÁO: Không thể chụp ảnh màn hình. Lỗi: {screenshot_e}")

            raise 

    def get_all_product_names(self):
        """Trả về danh sách tất cả các tên sản phẩm hiển thị trên trang sản phẩm."""
        product_elements = self.find_elements(self._product_names) # find_elements cũng sẽ chờ presence_of_all_elements_located
        names = [element.text for element in product_elements]
        print(f"DEBUG: Tìm thấy {len(names)} sản phẩm trên trang sản phẩm: {names}")
        return names

    def add_multiple_products_to_cart(self, num_products=3):
        """Thêm 'num_products' đầu tiên từ danh sách sản phẩm vào giỏ hàng."""
        product_names = self.get_all_product_names()
        if len(product_names) < num_products:
            print(f"CẢNH BÁO: Chỉ tìm thấy {len(product_names)} sản phẩm, nhưng yêu cầu thêm {num_products}. Sẽ thêm tất cả sản phẩm tìm thấy.")
            products_to_add = product_names
        else:
            products_to_add = product_names[:num_products]

        for product_name in products_to_add:
            self.add_product_to_cart(product_name)
        return products_to_add
        
    def click_shopping_cart_icon(self):
        """Nhấp vào biểu tượng giỏ hàng."""
        self.click_element(self._shopping_cart_link)
        print("Đã nhấp vào biểu tượng giỏ hàng.")