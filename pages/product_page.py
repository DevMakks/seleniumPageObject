from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_name = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(ProductPageLocators.PRODUCT_NAME)).text
        product_price = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(ProductPageLocators.PRODUCT_PRICE)).text
        add_to_cart_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(ProductPageLocators.ADD_TO_BASKET_BUTTON))
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()
        basket_total_in_inneralert = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(ProductPageLocators.BASKET_TOTAL_IN_INNERALERT)).text
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        assert product_name == product_name_in_alert
        assert product_price == basket_total_in_inneralert

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

        return True