from config.config import sorted_names_az, sorted_names_za, sorted_prices_lohi, sorted_prices_hilo
from conftest import inventory_page


def test_cart_functionality(logged_in_page, inventory_page):

    for i in range(1, 7):
        inventory_page.add_product_to_cart(i)
        assert inventory_page.get_cart_number() == i

    for i in range(6, 1, -1):
            inventory_page.remove_product_from_cart(i)
            assert inventory_page.get_cart_number() == i - 1

    inventory_page.remove_product_from_cart(1)
    assert inventory_page.cart_number_disappeared()

def test_goods_sorting(logged_in_page, inventory_page):

    inventory_page.click_filter_button("az")
    sorted_names = inventory_page.get_product_names()
    assert sorted_names == sorted_names_az

    inventory_page.click_filter_button("za")
    sorted_names = inventory_page.get_product_names()
    assert sorted_names == sorted_names_za

    inventory_page.click_filter_button("lohi")
    sorted_prices = inventory_page.get_product_prices()
    assert sorted_prices == sorted_prices_lohi

    inventory_page.click_filter_button("hilo")
    sorted_prices = inventory_page.get_product_prices()
    assert sorted_prices == sorted_prices_hilo

def test_product_card(logged_in_page, inventory_page):
    for i in range(0, 6):
        inventory_page.click_product_name(i)
        assert f"/inventory-item.html?id={i}" in inventory_page.page.url
        inventory_page.click_back_to_products()