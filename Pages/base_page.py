from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_page(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON), "User icon is missing, probably unauthorised user"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        assert self.is_element_present(
            *BasePageLocators.VIEW_BASKET), 'View basket button is missing'
        self.browser.find_element(*BasePageLocators.VIEW_BASKET).click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not present"

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, ignored_exceptions=[TimeoutException]).until_not(
                EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
