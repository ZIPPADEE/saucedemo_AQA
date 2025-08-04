#---URL---
base_url = "https://www.saucedemo.com/"
inventory_page_url = "https://www.saucedemo.com/inventory.html"
cart_url = "https://www.saucedemo.com/cart.html"
checkout1_url = "https://www.saucedemo.com/checkout-step-one.html"
checkout2_url = "https://www.saucedemo.com/checkout-step-two.html"
checkout_complete = "https://www.saucedemo.com/checkout-complete.html"

#---Username and password---
valid_user_1 = {
    "username": "standard_user",
    "password": "secret_sauce"
}

valid_user_2 = {
    "username": "visual_user",
}

valid_user_3 = {
    "username": "visual_user",
}

invalid_user = {
    "username": "invalid_user",
    "password": "invalid_password"
}

#---Goods list---
sorted_names_az = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

sorted_names_za = list(reversed(sorted_names_az))

sorted_prices_lohi = [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]

sorted_prices_hilo = list(reversed(sorted_prices_lohi))

#---Checkout info---
first_name = "John"
last_name = "Doe"
postal_code = "101000"

#---Checkout Prices---
all_goods_price = 140.34
empty_cart_price = 0.00