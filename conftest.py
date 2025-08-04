import pytest

from pages.checkout1_page import Checkout1Page
from pages.checkout2_page import Checkout2Page
from pages.inventory_page import InventoryPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from config.config import valid_user_1, inventory_page_url, first_name, last_name, postal_code

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout1_page(page):
    return Checkout1Page(page)

@pytest.fixture
def checkout2_page(page):
    return Checkout2Page(page)

@pytest.fixture
def checkout_complete_page(page):
    return CheckoutCompletePage(page)

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(valid_user_1["username"], valid_user_1["password"])
    return page

@pytest.fixture
def add_goods_to_cart(inventory_page):
    for i in range(1, 7):
        inventory_page.add_product_to_cart(i)
        assert inventory_page.get_cart_number() == i

@pytest.fixture
def fill_checkout1(checkout1_page):
    checkout1_page.fill(checkout1_page.first_name_field, first_name)
    checkout1_page.fill(checkout1_page.last_name_field, last_name)
    checkout1_page.fill(checkout1_page.postal_code_field, postal_code)
    checkout1_page.click(checkout1_page.continue_button)