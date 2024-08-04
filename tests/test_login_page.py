import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.links import PagesLinks


@pytest.mark.smoke
def test_login(browser):
    link = PagesLinks.LOGIN_LINK
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_pass()
    page.go_to_submit_button()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/header/div/ul/li[1]/a'))
    )
    browser.save_screenshot('result_scr.png')


@pytest.mark.smoke
def test_go_back_to_main(browser):
    link = PagesLinks.LOGIN_LINK
    page = LoginPage(browser, link)
    page.open()
    page.go_back_to_main()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]'))
    )
    browser.save_screenshot("result_back.png")


@pytest.mark.regression
def test_show_pass(browser):
    link = PagesLinks.LOGIN_LINK
    page = LoginPage(browser, link)
    page.open()
    page.go_to_pass()
    page.show_password()
    element = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element_value((By.XPATH, '//*[@id="password"]/input'), '12345')
    )
    browser.save_screenshot("show_pass_result.png")
