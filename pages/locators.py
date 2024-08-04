from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    OPEN_FIRST_PET = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button')
    LIKE_FIRST_PET = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]')
    FIRST_PET_COUNTER = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/span[2]')
    TYPE_DROPDOWN = (By.XPATH, '//*[@id="typesSelector"]')
    DOG_TYPE = (By.ID, 'pv_id_2_0')
    NAME_INPUT = (By.ID, 'petName')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    MAIN_ICON = (By.XPATH, '//*[@id="app"]/header/div/div')
    SHOW_PASS = (By.XPATH, '//*[@id="password"]/i')


class ProfilePageLocators:
    ADD_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    NEW_PET_NAME = (By.ID, 'name')
    NEW_PET_TYPE = (By.ID, 'typeSelector')
    TYPE_OPTION = (By.ID, 'pv_id_4_0')
    PROFILE_SUBMIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CHOOSE_AVATAR_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')
    SEND_AVA_FILE = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    ADD_AVATAR_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')
    QUIT_BTN = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a')


