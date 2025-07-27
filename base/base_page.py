from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement # Để gợi ý kiểu dữ liệu

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element_to_be_clickable(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Chờ cho một phần tử có thể nhấp được và trả về nó."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, url_check: str, timeout: int = 10) -> bool:
        """Chờ cho URL hiện tại chứa một chuỗi con cụ thể."""
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_check)
        )

    def open_url(self, url: str):
        """Mở URL đã cho. Hữu ích cho các Page Object cụ thể có thể điều hướng trực tiếp."""
        self.driver.get(url)

    def find_element(self, locator: tuple) -> WebElement:
        """
        Tìm một phần tử duy nhất bằng cách chờ sự hiện diện của nó.
        Tất cả các phương thức tương tác khác (click, send_keys, get_text) sẽ gọi phương thức này.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """Tìm nhiều phần tử bằng cách chờ sự hiện diện của tất cả chúng."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator: tuple):
        """Nhấp vào một phần tử sau khi nó có thể nhấp được."""
        self.wait_for_element_to_be_clickable(locator).click()

    def send_keys(self, locator: tuple, text: str):
        """Gửi văn bản đến một trường nhập liệu, xóa nội dung hiện có trước tiên."""
        element = self.find_element(locator) 
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator: tuple) -> str:
        """Lấy văn bản của một phần tử sau khi nó hiện diện."""
        return self.find_element(locator).text

    def get_current_url(self) -> str:
        """Trả về URL hiện tại của trang. Rất hữu ích cho việc xác minh URL trong kiểm thử."""
        return self.driver.current_url