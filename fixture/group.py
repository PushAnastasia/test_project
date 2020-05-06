

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.driver = self.app.driver
        self.open_add_contact_page()
        # fill Contact form
        self.driver.find_element(By.ID, "CompanyName").click()
        self.driver.find_element(By.ID, "CompanyName").send_keys(group.name)
        self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > .grey-block").click()
        # submit creation
        self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()

    def open_add_contact_page(self):
        self.driver = self.app.driver
        self.driver.find_element(By.CSS_SELECTOR, ".create-block .link-content").click()
        self.driver.find_element(By.LINK_TEXT, "Contact").click()