from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")

    ITEM_ADDED_ALERT = (
        By.CSS_SELECTOR, "#messages > .alert-success:first-child > .alertinner")

    BASKET_QUALIFIES_FOR_OFFER_ALERT = (
        By.CSS_SELECTOR, "#messages > .alert-success:second-child > .alertinner")

    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1:first-child")

    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

    BASKET_TOTAL_ALERT = (
        By.CSS_SELECTOR, "#messages > .alert-info > .alertinner")
