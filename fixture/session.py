from selenium.webdriver.common.by import By

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.driver = self.app.driver
        self.app.open_home_page()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email-address").click()
        self.driver.find_element(By.ID, "email-address").send_keys(username)
        self.driver.find_element(By.ID, "cpassword").click()
        self.driver.find_element(By.ID, "cpassword").send_keys(password)
        self.driver.find_element(By.ID, "btnLogin").click()
