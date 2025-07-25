from selenium.webdriver.common.by import By
from base.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_list = (By.CLASS_NAME, "inventory_item")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def get_product_list(self):
        return self.driver.find_elements(*self.product_list)

    def click_cart_icon(self):
        cart_icon_element = self.wait_for_element_to_be_clickable(self.cart_icon)
        cart_icon_element.click()