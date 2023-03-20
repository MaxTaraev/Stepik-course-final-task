from Pages.product_page import ProductPage
import time

# pytest -s -v --tb=line --language=en test_product_page.py


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    product_page = ProductPage(browser, link)
    product_page.open_page()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.should_be_item_added_to_cart_alert()
    product_page.should_be_correct_name_of_item_in_item_added_alert()
    product_page.should_be_basket_total_alert()
    product_page.should_be_correct_price_in_basket_total_alert()
