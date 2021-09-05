from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer"

@pytest.mark.parametrize('links', 
                                [
                                    link+'0',
                                    link+'1',
                                    link+'2',
                                    link+'3',
                                    link+'4',
                                    link+'5',
                                    link+'6',
                                    pytest.param(link+'7',
                                                 marks=pytest.mark.xfail),
                                    link+'8',
                                    link+'9'
                                ]
                        )   
def test_guest_can_add_product_to_basket(browser, links):
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_product_to_basket()
    time.sleep(5)

@pytest.mark.xfail
@pytest.mark.parametrize('link', [link+'0'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', [link+'0'])
def test_guest_cant_see_success_mesage(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
@pytest.mark.parametrize('link', [link+'0'])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    time.sleep(10)
    page.should_be_desappeared_success_message()

def test_guest_should_see_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.new_tests
def  test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_text_your_basket_is_empty()