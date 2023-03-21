from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # Добавить текущий товар в корзину
    def add_item_to_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART), '"Add to cart" button is missing'
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    # Найти и вернуть название товара
    def get_item_name(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_NAME), 'Product name is missing'
        return self.browser.find_element(
            *ProductPageLocators.ITEM_NAME)

    # Найти и вернуть цену товара
    def get_item_price(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_PRICE), 'Product price is missing'
        return self.browser.find_element(
            *ProductPageLocators.ITEM_PRICE)

    # НЕГАТИВНАЯ проверка на то, что нет сообщения о добавлении товара в корзину
    def should_not_be_added_to_cart_alert(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEM_ADDED_ALERT), "Added to cart alert is presented, expected not to be"
        print('Succes alert is not presented')

    # Должно пропасть сообщение о том, что товар добавлен в корзину
    def should_disappear_added_to_cart_alert(self):
        assert self.is_disappeared(
            *ProductPageLocators.ITEM_ADDED_ALERT), "Added to cart alert did not disappear"

    # Есть ли сообщение о том, что товар добавлен в корзину
    def should_be_item_added_to_cart_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_ADDED_ALERT), 'Added to cart alert is missing'

    # Правильное ли название товара в сообщение о его добавлении
    def should_be_correct_name_of_item_in_item_added_alert(self):
        assert self.get_item_name().text == self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED_ALERT).text, 'Incorrect name of item in added to cart alert'

    # Есть ли сообщение со стоимостью корзины
    def should_be_basket_total_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_TOTAL_ALERT), 'Basket total alert is missing'

    # Правильная ли цена в сообщении о стоимости корзины
    def should_be_correct_price_in_basket_total_alert(self):
        assert self.get_item_price().text == self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_ALERT).text, 'Incorrect price of item in basket total alert'
