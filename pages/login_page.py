from pages.base_page import BasePage
from config.config import base_url

class LoginPage(BasePage):
    URL = base_url
    username_field = "#user-name"
    password_field = "#password"
    login_button = "#login-button"

    def open(self):
        self.goto(self.URL)

    def login(self, username, password):
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.login_button)