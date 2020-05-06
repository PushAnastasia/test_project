from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome('C:\Program Files\Chromedriver\chromedriver.exe')
        self.vars = {}
        self.session = SessionHelper(self)

    def create_contact(self, group):
        self.open_add_contact_page()
        # fill Contact form
        self.driver.find_element(By.ID, "CompanyName").click()
        self.driver.find_element(By.ID, "CompanyName").send_keys(group.name)
        self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > .grey-block").click()
        # submit creation
        self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()

    def open_add_contact_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".create-block .link-content").click()
        self.driver.find_element(By.LINK_TEXT, "Contact").click()

    def open_home_page(self):
        self.driver.get("https://skyt.qa.sharp.nixdev.co/")
        self.driver.set_window_size(1936, 1056)

    def destroy(self):
        self.driver.quit()