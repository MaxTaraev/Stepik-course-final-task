from Pages.product_page import ProductPage
import time
import pytest

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


def test_guest_can_add_product_to_basket(browser, promo):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    # print(link)

    product_page = ProductPage(browser, link)
    product_page.open_page()

    product_page.should_not_be_added_to_cart_alert()

    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    time.sleep(2)
    product_page.should_be_item_added_to_cart_alert()
    product_page.should_be_correct_name_of_item_in_item_added_alert()
    product_page.should_be_basket_total_alert()
    product_page.should_be_correct_price_in_basket_total_alert()
