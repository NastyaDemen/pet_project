import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.links import PagesLinks


def test_go_to_login_page(browser):
    link = PagesLinks.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result5.png')


def test_open_first_pet(browser):
    link = PagesLinks.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_pet()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div[1]/div[1]/div/div/div[1]'))
    )
    browser.save_screenshot('result_pet.png')


def test_unauthorized_user_cannot_like_pet(browser):
    link = PagesLinks.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    initial_likes_quantity = page.define_likes_counter_value()
    page.like_pet()
    browser.save_screenshot('result_like.png')
    changed_likes_quantity = page.define_likes_counter_value()
    assert initial_likes_quantity == changed_likes_quantity


def test_filter_by_type(browser):
    link = PagesLinks.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.expand_type_dropdown()
    page.choose_dog()
    time.sleep(2)
    browser.save_screenshot('filtration_result.png')


def test_filter_by_name(browser):
    link = PagesLinks.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.enter_pet_name()
    time.sleep(2)
    browser.save_screenshot('filter_by_name_result.png')


def test_clear_filter_by_name(browser):
    link = PagesLinks.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.enter_pet_name()
    page.clear_pet_name()
    time.sleep(2)
    element = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, 'petName'), '')
    )
    browser.save_screenshot('clear_result.png')
