from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), 'Basket has items'

    def should_be_basket_empty_text(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT), 'Basket empty text is missing'
