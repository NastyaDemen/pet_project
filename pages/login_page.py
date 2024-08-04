from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('Nastya@test.com')

    def go_to_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('12345')

    def go_to_submit_button(self):
        login_submit_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_submit_button.submit()

    def go_back_to_main(self):
        main_icon = self.browser.find_element(*LoginPageLocators.MAIN_ICON)
        main_icon.click()

    def show_password(self):
        show_pass_btn = self.browser.find_element(*LoginPageLocators.SHOW_PASS).click()