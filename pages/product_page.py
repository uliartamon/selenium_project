import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    '''def check_add_to_basket_is_presented(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Add button was not found'''

    def check_add_to_basket_button(self):
        
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        print('\nProduct added to basket')

    def get_product_info(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return price, product_name
    
    def get_alert_info(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_name_info = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_INFO).text
        return basket_price, product_name_info