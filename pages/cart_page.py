from pages.base_page import BasePage
from config.config import cart_url

class CartPage(BasePage):
    URL = cart_url
    continue_shopping_button = "#continue-shopping"
    checkout_button = "#checkout"
    cart_button = "[data-test='shopping-cart-link']"

    def open_cart(self):
        self.goto(self.URL)

    def continue_shopping(self):
        self.click(self.continue_shopping_button)

    def checkout(self):
        self.click(self.checkout_button)

    def click_cart_button(self):
        self.click(self.cart_button)