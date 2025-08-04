from playwright.sync_api import Page

class BasePage:
    def __init__(self, page):
        self.page = page

    #--- Common locators---
    remove_from_cart1 = "#remove-sauce-labs-backpack"
    remove_from_cart2 = "#remove-sauce-labs-bike-light"
    remove_from_cart3 = "#remove-sauce-labs-bolt-t-shirt"
    remove_from_cart4 = "#remove-sauce-labs-fleece-jacket"
    remove_from_cart5 = "#remove-sauce-labs-onesie"
    remove_from_cart6 = "#remove-test\\.allthethings\\(\\)-t-shirt-\\(red\\)"
    cart_number = "[data-test='shopping-cart-badge']"
    product_name_locator5 = "text=Sauce Labs Backpack" #4
    product_name_locator1 = "text=Sauce Labs Bike Light" #0
    product_name_locator2 = "text=Sauce Labs Bolt T-Shirt" #1
    product_name_locator6 = "text=Sauce Labs Fleece Jacket" #5
    product_name_locator3 = "text=Sauce Labs Onesie" #2
    product_name_locator4 = "text=Test.allTheThings() T-Shirt (Red)" #3
    login_error = "[data-test='error']"
    error_close_button = "[data-test='error-button']"
    error_message_container = ".error-message-container"
    cancel_button = "#cancel"

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)

    def goto(self, url):
        self.page.goto(url)

    def is_visible(self, locator):
        return self.page.is_visible(locator)

    def get_text(self, locator):
        self.page.wait_for_selector(locator, state="visible", timeout=10000)
        text = self.page.text_content(locator)
        return text.strip() if text else ""

    def remove_product_from_cart(self, product_number):
        locators = {
            1:self.remove_from_cart1,
            2: self.remove_from_cart2,
            3: self.remove_from_cart3,
            4: self.remove_from_cart4,
            5: self.remove_from_cart5,
            6: self.remove_from_cart6
        }
        self.click(locators[product_number])

    def get_cart_number(self):
        text = self.get_text(self.cart_number)
        return int(text) if text.isdigit() else 0

    def cart_number_disappeared(self):
        return not self.page.is_visible(self.cart_number)

    def click_product_name(self, product_number):
        locators = {
            0: self.product_name_locator1,
            1: self.product_name_locator2,
            2: self.product_name_locator3,
            3: self.product_name_locator4,
            4: self.product_name_locator5,
            5: self.product_name_locator6,
        }
        self.click(locators[product_number])

    def is_error_visible(self, timeout=2000):
        return self.page.wait_for_selector(self.login_error, timeout=timeout).is_visible()

    def get_error_message_text(self):
        return self.page.text_content(self.login_error)

    def close_error_message(self):
        self.click(self.error_close_button)

    def is_error_message_disappeared(self):
        return self.page.is_visible(self.error_message_container)

    def click_cancel_button(self):
        self.click(self.cancel_button)