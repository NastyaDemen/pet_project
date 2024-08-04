from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_pet(self):
        pet = self.browser.find_element(*MainPageLocators.OPEN_FIRST_PET).click()

    def like_pet(self):
        like_pet = self.browser.find_element(*MainPageLocators.LIKE_FIRST_PET).click()

    def expand_type_dropdown(self):
        filter_by_type = self.browser.find_element(*MainPageLocators.TYPE_DROPDOWN).click()

    def choose_dog(self):
        choose_dog_type = self.browser.find_element(*MainPageLocators.DOG_TYPE).click()

    def enter_pet_name(self):
        filter_by_name = self.browser.find_element(*MainPageLocators.NAME_INPUT)
        filter_by_name.send_keys('12345')
        filter_by_name.send_keys(Keys.ENTER)

    def clear_pet_name(self):
        filter_input = self.browser.find_element(*MainPageLocators.NAME_INPUT)
        filter_input.clear()
        filter_input.send_keys(Keys.ENTER)

    def define_likes_counter_value(self):
        counter = self.browser.find_element(*MainPageLocators.FIRST_PET_COUNTER)
        quantity = counter.text
        return quantity
