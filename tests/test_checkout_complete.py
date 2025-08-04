def test_back_home(logged_in_page, checkout_complete_page):
    checkout_complete_page.open_checkout_complete()
    checkout_complete_page.click_back_home()
    assert "/inventory.html" in checkout_complete_page.page.url