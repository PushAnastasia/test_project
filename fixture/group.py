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
        self.contact_cache = None

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

    def select_contact_by_index(self, index):
        self.driver = self.app.driver
        self.driver.find_elements(By.CSS_SELECTOR, ".list-body .text-cell .icon-check")[index].click()

    def inactive_first_contact(self):
        self.driver = self.app.driver
        self.inactive_contact_by_index(0)

    def inactive_contact_by_index(self, index):
        self.driver = self.app.driver
        self.open_address_book_page()
        self.select_contact_by_index(index)
        # submit inactivation
        self.driver.find_element(By.LINK_TEXT, "Activities").click()
        self.driver.find_element(By.LINK_TEXT, "Set Inactive").click()
        self.driver.find_element(By.CSS_SELECTOR, ".popup-content .btn-delete").click()
        self.contact_cache = None

    def open_address_book_page(self):
        self.driver = self.app.driver
        if self.driver.current_url.endswith("AddressBook?customertype=0&groupid=null") and len(self.driver.find_elements(By.LINK_TEXT, "Add Contact")) > 0:
            return
        self.driver.find_element(By.ID, "AddressBook").click()
        self.driver.find_element(By.ID, "AllContacts").click()

    def modify_first_contact(self):
        self.driver = self.app.driver
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_group_data):
        self.driver = self.app.driver
        self.open_address_book_page()
        # select first contact
        self.driver.find_elements(By.LINK_TEXT, "TestClient")[index].click()
        # open edit contact page
        self.driver.find_element(By.CSS_SELECTOR, ".page-block .list-footer .btn-holder .btn-edit").click()
        self.driver.implicitly_wait(10)
        # edit contact form
        self.fill_contact_form(new_group_data)
        # submit modification
        self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()
        self.contact_cache = None

    def count(self):
        self.driver = self.app.driver
        self.open_address_book_page()
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".list-body .text-cell .icon-check"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.driver = self.app.driver
            self.open_address_book_page()
            self.contact_cache = []
            for element in self.driver.find_elements(By.CSS_SELECTOR, ".list-body .col-organization"):
                text = element.text
    #            id = element.find_element(By.CSS_SELECTOR, ".list-body .col-checkbox .text-cell .checkbox-container .mvc-grid-checkbox").get_attribute("value")
                self.contact_cache.append(Group(name=text, id=id))
        return list(self.contact_cache)
