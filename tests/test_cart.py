from conftest import add_goods_to_cart


def test_continue_shopping(add_goods_to_cart, cart_page):
    cart_page.open_cart()
    cart_page.continue_shopping()
    assert "/inventory" in cart_page.page.url

def test_checkout(add_goods_to_cart, cart_page):
    cart_page.open_cart()
    cart_page.checkout()
    assert "/checkout-step-one.html" in cart_page.page.url

def test_remove_from_cart(add_goods_to_cart, cart_page):
    cart_page.open_cart()
    for i in range(6, 1, -1):
            cart_page.remove_product_from_cart(i)
            assert cart_page.get_cart_number() == i - 1

def test_product_card_cart(add_goods_to_cart, cart_page):
    cart_page.open_cart()
    for i in range(0, 6):
        cart_page.click_product_name(i)
        assert f"/inventory-item.html?id={i}" in cart_page.page.url
        cart_page.click_cart_button()