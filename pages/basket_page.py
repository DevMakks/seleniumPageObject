from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            'Basket is not empty, but should be!'
    
    def should_be_text_your_basket_is_empty(self):
        assert "Your basket is empty" in \
             self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text,\
                'Message that basket is empty is not finded!'