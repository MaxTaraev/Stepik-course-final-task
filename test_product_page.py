from Pages.product_page import ProductPage
import time
import pytest
from Pages.login_page import LoginPage
from Pages.basket_page import BasketPage

# pytest -s -v --tb=line --language=en test_product_page.py


# @pytest.mark.parametrize('promo', [
#     '?promo=offer0',
#     '?promo=offer1',
#     '?promo=offer2',
#     '?promo=offer3',
#     '?promo=offer4',
#     '?promo=offer5',
#     '?promo=offer6',
#     pytest.param('?promo=offer7', marks=pytest.mark.xfail(
#         reason="Wrong item name in added to cart alert")),
#     '?promo=offer8',
#     '?promo=offer9'
# ])


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    # print(link)

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    # time.sleep(2)
    product_page.should_be_item_added_to_cart_alert()
    product_page.should_be_correct_name_of_item_in_item_added_alert()
    product_page.should_be_basket_total_alert()
    product_page.should_be_correct_price_in_basket_total_alert()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

    product_page = ProductPage(browser, link, timeout=0)
    product_page.open_page()
    product_page.add_item_to_cart()
    product_page.should_not_be_added_to_cart_alert()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

    product_page = ProductPage(browser, link, timeout=0)
    product_page.open_page()
    product_page.should_not_be_added_to_cart_alert()


@pytest.mark.skip
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


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_item_in_basket()
    basket_page.should_be_basket_empty_text()
