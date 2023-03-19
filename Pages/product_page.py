from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_cart(self):
        assert self.click_on_element(
            *ProductPageLocators.ADD_TO_CART), '"Add to cart" button is not present'

    def item_added_to_cart_alert(self):
        # 3 абсолютно одинаковых алерта, разный только текст внутри них. Использовать find_elements? 
        pass
