from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.director import DirectorHelper


class Application:

    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome('C:\Program Files\Chromedriver\chromedriver.exe')
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie('C:\Program Files\IEdriver\IEDriverServer.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.implicitly_wait(5)
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.director = DirectorHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.driver.get("https://skyt.qa.sharp.nixdev.co/")
        self.driver.set_window_size(1936, 1056)

    def destroy(self):
        self.driver.quit()

    def open_directors_page(self):
        self.driver.find_element(By.ID, "Settings").click()
        self.driver.find_element(By.LINK_TEXT, "People").click()

