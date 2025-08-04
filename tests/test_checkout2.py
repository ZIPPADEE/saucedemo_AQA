from config.config import all_goods_price, empty_cart_price


def test_finish_button(logged_in_page, checkout2_page):
    checkout2_page.open_checkout2()
    checkout2_page.click_finish_button()
    assert "/checkout-complete.html" in checkout2_page.page.url

def test_cancel_button(logged_in_page, checkout2_page):
    checkout2_page.open_checkout2()
    checkout2_page.click_cancel_button()
    assert "/inventory.html" in checkout2_page.page.url

def test_price_value_max(logged_in_page, add_goods_to_cart, checkout2_page):
    checkout2_page.open_checkout2()
    actual_price = checkout2_page.get_total_price()
    assert actual_price == all_goods_price

def test_price_value_min(logged_in_page, checkout2_page):
    checkout2_page.open_checkout2()
    actual_price = checkout2_page.get_total_price()
    assert actual_price == empty_cart_price