from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REG_FORM = (By.CSS_SELECTOR, "form#register_form.well")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    PRODUCT_NAME_INFO = (By.CSS_SELECTOR, '#messages .alert-success .alertinner strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages .alert-info .alertinner p strong')
