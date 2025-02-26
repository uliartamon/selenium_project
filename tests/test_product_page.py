import time
import pytest
from pages.product_page import ProductPage


URLS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('URL', URLS) 
def test_add_to_basket(browser, URL):
    product_page = ProductPage(browser, URL)
    product_page.open()
    price, product_name = product_page.get_product_info()
    product_page.check_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    time.sleep(2)
    basket_price, product_name_info = product_page.get_alert_info()
    assert price == basket_price, f'Basket price {basket_price} not equal product price {price}'
    assert product_name == product_name_info, f'Product name info {product_name_info} not equal product name {product_name}'