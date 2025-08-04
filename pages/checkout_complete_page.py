from pages.base_page import BasePage
from config.config import checkout_complete


class CheckoutCompletePage(BasePage):
    URL = checkout_complete
    back_home_button = "#back-to-products"

    def open_checkout_complete(self):
        self.goto(self.URL)

    def click_back_home(self):
        self.click(self.back_home_button)