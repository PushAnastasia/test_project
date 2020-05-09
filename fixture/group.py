from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.driver = self.app.driver
        self.open_add_contact_page()
        self.fill_contact_form(group)
        # submit creation
        self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()

    def fill_contact_form(self, group):
        self.driver = self.app.driver
        if group.name is not None:
            self.driver.find_element(By.ID, "CompanyName").click()
            self.driver.find_element(By.ID, "CompanyName").clear()
            self.driver.find_element(By.ID, "CompanyName").send_keys(group.name)
            self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > .grey-block").click()

    def open_add_contact_page(self):
        self.driver = self.app.driver
        self.driver.find_element(By.CSS_SELECTOR, ".create-block .link-content").click()
        self.driver.find_element(By.LINK_TEXT, "Contact").click()

    def inactive_first_contact(self):
        self.driver = self.app.driver
        self.opend_address_book_page()
        # select first contact
        self.driver.find_element(By.CSS_SELECTOR, ".list-body .text-cell .icon-check").click()
        # submit inactivation
        self.driver.find_element(By.LINK_TEXT, "Activities").click()
        self.driver.find_element(By.LINK_TEXT, "Set Inactive").click()
        self.driver.find_element(By.CSS_SELECTOR, ".popup-content .btn-delete").click()

    def opend_address_book_page(self):
        self.driver = self.app.driver
        self.driver.find_element(By.ID, "AddressBook").click()
        self.driver.find_element(By.ID, "AllContacts").click()

    def modify_first_contact(self, new_group_data):
        self.driver = self.app.driver
        self.opend_address_book_page()
        # select first contact
        self.driver.find_element(By.LINK_TEXT, "New Contact2").click()
        # open edit contact page
        self.driver.find_element(By.CSS_SELECTOR, ".page-block .list-footer .btn-holder .btn-edit").click()
        self.driver.implicitly_wait(10)
        # edit contact form
        self.fill_contact_form(new_group_data)
        # submit modification
        self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()
