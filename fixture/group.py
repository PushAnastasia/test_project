from selenium.webdriver.common.by import By
from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.driver = self.app.driver
        self.driver.find_element(By.CSS_SELECTOR, ".header .logo").click()
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
        self.open_address_book_page()
        # select first contact
        self.driver.find_element(By.CSS_SELECTOR, ".list-body .text-cell .icon-check").click()
        # submit inactivation
        self.driver.find_element(By.LINK_TEXT, "Activities").click()
        self.driver.find_element(By.LINK_TEXT, "Set Inactive").click()
        self.driver.find_element(By.CSS_SELECTOR, ".popup-content .btn-delete").click()

    def open_address_book_page(self):
        self.driver = self.app.driver
        if self.driver.current_url.endswith("AddressBook?customertype=0&groupid=null") and len(self.driver.find_elements(By.LINK_TEXT, "Add Contact")) > 0:
            return
        self.driver.find_element(By.ID, "AddressBook").click()
        self.driver.find_element(By.ID, "AllContacts").click()

    def modify_first_contact(self, new_group_data):
        self.driver = self.app.driver
        self.open_address_book_page()
        # select first contact
        self.driver.find_element(By.LINK_TEXT, "TestClient").click()
        # open edit contact page
        self.driver.find_element(By.CSS_SELECTOR, ".page-block .list-footer .btn-holder .btn-edit").click()
        self.driver.implicitly_wait(10)
        # edit contact form
        self.fill_contact_form(new_group_data)
        # submit modification
        self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()

    def count(self):
        self.driver = self.app.driver
        self.open_address_book_page()
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".list-body .text-cell .icon-check"))

    def get_contact_list(self):
        self.driver = self.app.driver
        self.open_address_book_page()
        contacts = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, ".list-body .col-organization"):
            text =  element.text
    #        id = element.find_element(By.CSS_SELECTOR, ".list-body .col-checkbox .text-cell .checkbox-container .mvc-grid-checkbox").get_attribute("value")
            contacts.append(Group(name=text, id=id))
        return contacts
