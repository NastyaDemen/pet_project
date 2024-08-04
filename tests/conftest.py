import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import LoginPageLocators


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    browser.get('http://34.141.58.52:8080/#/login')
    login_input = browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys('Nastya@test.com')
    password_input = browser.find_element(*LoginPageLocators.LOGIN_PASS).send_keys('12345')
    submit_button = browser.find_element(*LoginPageLocators.LOGIN_BTN).submit()
