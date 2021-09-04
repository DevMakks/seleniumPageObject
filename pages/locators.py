from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form1")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form1")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages>div:nth-of-type(1) .alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    BASKET_TOTAL_IN_INNERALERT = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success.fade.in>div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')