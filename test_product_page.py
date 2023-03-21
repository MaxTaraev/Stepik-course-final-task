from Pages.product_page import ProductPage
import time
import pytest
from Pages.login_page import LoginPage
from Pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        email = str(time.time()) + "@fakemail.org"

        login_page = LoginPage(browser, link)
        login_page.open_page()
        login_page.register_new_user(email=email, password='nt&aC4JaI72x')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

        product_page = ProductPage(browser, link)
        product_page.open_page()
        product_page.add_item_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_item_added_to_cart_alert()
        product_page.should_be_correct_name_of_item_in_item_added_alert()
        product_page.should_be_basket_total_alert()
        product_page.should_be_correct_price_in_basket_total_alert()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

        product_page = ProductPage(browser, link, timeout=0)
        product_page.open_page()
        product_page.should_not_be_added_to_cart_alert()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_item_added_to_cart_alert()
    product_page.should_be_correct_name_of_item_in_item_added_alert()
    product_page.should_be_basket_total_alert()
    product_page.should_be_correct_price_in_basket_total_alert()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

    product_page = ProductPage(browser, link, timeout=0)
    product_page.open_page()
    product_page.should_not_be_added_to_cart_alert()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

    product_page = ProductPage(browser, link, timeout=0)
    product_page.open_page()
    product_page.add_item_to_cart()
    product_page.should_not_be_added_to_cart_alert()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

    product_page = ProductPage(browser, link, timeout=0)
    product_page.open_page()
    product_page.add_item_to_cart()
    product_page.should_disappear_added_to_cart_alert()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_item_in_basket()
    basket_page.should_be_basket_empty_text()
