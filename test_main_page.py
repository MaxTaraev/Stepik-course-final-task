from Pages.main_page import MainPage
from Pages.login_page import LoginPage

# pytest -v --tb=line --language=en test_main_page.py


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
