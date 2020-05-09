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

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".user-block .link-content").click()
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()

    def ensure_logout(self):
        self.driver = self.app.driver
        if len(self.driver.find_elements(By.LINK_TEXT, "Hello,")) > 0:
            self.logout()
