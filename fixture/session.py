

class SessionHelper:
    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email-address").click()
        self.driver.find_element(By.ID, "email-address").send_keys(username)
        self.driver.find_element(By.ID, "cpassword").click()
        self.driver.find_element(By.ID, "cpassword").send_keys(password)
        self.driver.find_element(By.ID, "btnLogin").click()
