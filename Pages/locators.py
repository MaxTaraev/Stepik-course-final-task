from selenium.webdriver.common.by import By


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")

    ITEM_ADDED_ALERT = (
        By.CSS_SELECTOR, "#messages > .alert-success:first-child > .alertinner strong")

    BASKET_QUALIFIES_FOR_OFFER_ALERT = (
        By.CSS_SELECTOR, "#messages > .alert-success:second-child > .alertinner")

    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1:first-child")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

    BASKET_TOTAL_ALERT = (
        By.CSS_SELECTOR, "#messages > .alert-info > .alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, ".content > #content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
