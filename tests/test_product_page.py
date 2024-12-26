from pages.product_page import ProductPage


URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

def test_add_to_basket_is_presented(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.check_add_to_basket_is_presented()

def test_add_to_basket_is_visible(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()
    product_page.check_add_to_basket_button()
    product_page.solve_quiz_and_get_code()

    price = product_page.check_product_price()
    basket_sum = product_page.check_basket_sum()

    assert basket_sum == price, f'The basket price = {basket_sum} does not match the product price = {price}.'
