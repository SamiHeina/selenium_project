from selenium.webdriver.common.by import By

class ApplyPage:
    def __init__(self, driver):
        self.driver = driver
        self.apply_btn = (By.ID, "apply-btn")
        self.confirmation_msg = (By.ID, "confirmation-msg")

    def click_apply(self):
        self.driver.find_element(*self.apply_btn).click()





