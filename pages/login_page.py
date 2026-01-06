from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")

    def login(self, user, pwd):

        username_input = self.driver.find_element(*self.username)
        for char in user:
            username_input.send_keys(char)
            time.sleep(0.2)

        password_input = self.driver.find_element(*self.password)
        for char in pwd:
            password_input.send_keys(char)
            time.sleep(0.2)

        self.driver.find_element(*self.login_button).click()
        print("🔹 Logged in")
        time.sleep(1)




