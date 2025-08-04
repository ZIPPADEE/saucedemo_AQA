from pages.base_page import BasePage
from config.config import checkout2_url


class Checkout2Page(BasePage):
    URL = checkout2_url
    finish_button = "#finish"
    price_total = "[data-test='total-label']"

    def open_checkout2(self):
        self.goto(self.URL)

    def click_finish_button(self):
        self.click(self.finish_button)

    def get_total_price(self):
        text = self.page.locator(self.price_total).text_content().strip()
        price_text = text.replace("Total: ", "").replace("$", "").strip()
        return float(price_text)