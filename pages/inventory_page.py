from itertools import count

from playwright.sync_api import Expect

from pages.base_page import BasePage
from config.config import inventory_page_url

class InventoryPage(BasePage):
    inventory_url = inventory_page_url
    add_to_cart1 = "#add-to-cart-sauce-labs-backpack"
    add_to_cart2 = "#add-to-cart-sauce-labs-bike-light"
    add_to_cart3 = "#add-to-cart-sauce-labs-bolt-t-shirt"
    add_to_cart4 = "#add-to-cart-sauce-labs-fleece-jacket"
    add_to_cart5 = "#add-to-cart-sauce-labs-onesie"
    add_to_cart6 = "#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)"
    sort_container = "[data-test='product-sort-container']"
    back_to_products = "#back-to-products"

    def add_product_to_cart(self, product_number):
        locators = {
            1:self.add_to_cart1,
            2: self.add_to_cart2,
            3: self.add_to_cart3,
            4: self.add_to_cart4,
            5: self.add_to_cart5,
            6: self.add_to_cart6
        }
        self.click(locators[product_number])

    def open_inventory(self):
        self.page.goto(self.inventory_url)

    def click_filter_button(self, option_value):
        self.page.select_option(self.sort_container, value=option_value)

    def get_product_names(self):
        elements = self.page.locator(".inventory_item_name")
        cnt = elements.count()
        names = []
        for i in range(cnt):
            names.append(elements.nth(i).text_content().strip())
        return names

    def get_product_prices(self):
        elements = self.page.locator(".inventory_item_price")
        cnt = elements.count()
        prices = []
        for i in range(cnt):
            text = elements.nth(i).text_content().strip()
            price = float(text.replace("$", ""))
            prices.append(price)
        return prices

    def click_back_to_products(self):
        self.click(self.back_to_products)
