from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REG_FORM = (By.CSS_SELECTOR, "form#register_form.well")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    BASKET_SUM = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs')