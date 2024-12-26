import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def check_add_to_basket_is_presented(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Add button was not found'

    def check_add_to_basket_button(self):
        
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        print('\nProduct added to basket')

    def check_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price.strip()
    
    def check_basket_sum(self):
        basket_sum = self.browser.find_element(*ProductPageLocators.BASKET_SUM).text
        return basket_sum.split('\n')[0].split(':')[-1].strip()