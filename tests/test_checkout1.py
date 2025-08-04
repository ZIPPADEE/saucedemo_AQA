from config.config import first_name, last_name, postal_code

def test_checkout_valid_fields(add_goods_to_cart, checkout1_page):
    checkout1_page.open_checkout()
    checkout1_page.fill_info(first_name, last_name, postal_code)
    assert "/checkout-step-two.html" in checkout1_page.page.url

def test_checkout_invalid_name(add_goods_to_cart, checkout1_page):
    checkout1_page.open_checkout()
    checkout1_page.fill_info("", last_name, postal_code)
    assert checkout1_page.is_error_visible()

    expected_error_text = "Error: First Name is required"
    actual_error = checkout1_page.get_error_message_text()
    assert expected_error_text == actual_error

    checkout1_page.close_error_message()
    assert checkout1_page.is_error_message_disappeared()

def test_checkout_invalid_last_name(add_goods_to_cart, checkout1_page):
    checkout1_page.open_checkout()
    checkout1_page.fill_info(first_name, "", postal_code)
    assert checkout1_page.is_error_visible()

    expected_error_text = "Error: Last Name is required"
    actual_error = checkout1_page.get_error_message_text()
    assert expected_error_text == actual_error

    checkout1_page.close_error_message()
    assert checkout1_page.is_error_message_disappeared()

def test_checkout_invalid_postal_code(add_goods_to_cart, checkout1_page):
    checkout1_page.open_checkout()
    checkout1_page.fill_info(first_name, last_name, "")
    assert checkout1_page.is_error_visible()

    expected_error_text = "Error: Postal Code is required"
    actual_error = checkout1_page.get_error_message_text()
    assert expected_error_text == actual_error

    checkout1_page.close_error_message()
    assert checkout1_page.is_error_message_disappeared()

def test_checkout_cancel_button(logged_in_page, checkout1_page):
    checkout1_page.open_checkout()
    checkout1_page.click_cancel_button()
    assert "/cart.html" in checkout1_page.page.url