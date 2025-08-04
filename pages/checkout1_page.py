from pages.base_page import BasePage
from config.config import checkout1_url

class Checkout1Page(BasePage):
    URL = checkout1_url
    first_name_field = "#first-name"
    last_name_field = "#last-name"
    postal_code_field = "#postal-code"
    continue_button = "#continue"

    def open_checkout(self):
        self.goto(self.URL)

    def fill_info(self, first_name, last_name, postal_code):
        self.fill(self.first_name_field, first_name)
        self.fill(self.last_name_field, last_name)
        self.fill(self.postal_code_field, postal_code)
        self.click(self.continue_button)