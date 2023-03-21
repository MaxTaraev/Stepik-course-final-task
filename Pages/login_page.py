from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Not login url"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is missing"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Registration form is missing"

    def register_new_user(self, email, password):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_EMAIL), "Email field is missing"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD), "Password field is missing"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRM), "Confirm password field is missing"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_BUTTON), "'Register' button is missing"
        self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
