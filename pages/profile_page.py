from .locators import ProfilePageLocators
from .base_page import BasePage


class ProfilePage(BasePage):
    def go_to_new_pet_profile(self):
        go_to_new_pet = self.browser.find_element(*ProfilePageLocators.ADD_BTN).click()

    def enter_pet_name(self):
        new_pet_name = self.browser.find_element(*ProfilePageLocators.NEW_PET_NAME)
        new_pet_name.send_keys('Molly')

    def go_to_type_dropdown(self):
        type_dropdown = self.browser.find_element(*ProfilePageLocators.NEW_PET_TYPE).click()

    def choose_type(self):
        select_type = self.browser.find_element(*ProfilePageLocators.TYPE_OPTION).click()

    def create_pet(self):
        submit_form = self.browser.find_element(*ProfilePageLocators.PROFILE_SUBMIT_BTN).click()

    def go_to_choose_avatar(self):
        go_to_choose_avatar = self.browser.find_element(*ProfilePageLocators.CHOOSE_AVATAR_BTN).click()

    def send_ava_file(self):
        send_ava_file = self.browser.find_element(*ProfilePageLocators.SEND_AVA_FILE)
        send_ava_file.send_keys(r"C:\Users\anastasiyadziamentsy\PycharmProjects\pet_project\tests\molly2.jpg")

    def quit(self):
        quit_profile = self.browser.find_element(*ProfilePageLocators.QUIT_BTN).click()
