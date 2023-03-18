# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import time
# import math

class BasePage():
    def __init__(self, browser, url) -> None:
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
