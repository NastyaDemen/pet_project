import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.profile_page import ProfilePage
from pages.links import PagesLinks

@pytest.mark.smoke
def test_create_pet(browser, login):
    link = PagesLinks.PROFILE_PAGE_LINK
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_new_pet_profile()
    page.enter_pet_name()
    page.go_to_type_dropdown()
    page.choose_type()
    page.create_pet()
    time.sleep(2)
    page.go_to_choose_avatar()
    time.sleep(5)
    page.send_ava_file()
    page.go_to_choose_avatar()
    element = WebDriverWait(browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button'))
    )
    browser.save_screenshot('result_pet_added.png')


def test_quite(browser, login):
    link = PagesLinks.PROFILE_PAGE_LINK
    page = ProfilePage(browser, link)
    page.quit()
    browser.save_screenshot('result_quite.png')