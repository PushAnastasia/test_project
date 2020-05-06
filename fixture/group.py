from selenium.webdriver.common.by import By

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

    def inactive_first_contact(self):
        self.driver = self.app.driver
        # open address book page
        self.driver.find_element(By.LINK_TEXT, "Address Book").click()
        self.driver.find_element(By.ID, "AllContacts").click()
        # select first contact
        self.driver.find_element(By.NAME, "contacts").click()
        # submit inactivation
        self.driver.find_element(By.LINK_TEXT, "Activities").click()
        self.driver.find_element(By.LINK_TEXT, "Set Inactive").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn .btn-delete .btn-submit-confirm-dialog").click()