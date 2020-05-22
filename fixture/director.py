from selenium.webdriver.common.by import By
from model.director import Director


class DirectorHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        self.driver = self.app.driver
        if text is not None:
            self.driver.find_element(By.Name, field_name).click()
            self.driver.find_element(By.Name, field_name).clear()
            self.driver.find_element(By.Name, field_name).send_keys(test)

    director_cache = None

    def get_director_list(self):
        if self.director_cache is None:
            self.driver = self.app.driver
            self.app.open_director_page()
            self.director_cache = []
            for row in driver.find_elements(By.CSS_SELECTOR, ".list-body .col-firstname,lastname"):
                names = row.find_element(By.CSS_SELECTOR, ".list-body .col-firstname,lastname").text.split()
                firstname = names[0]
                lastname = names[1]
                id_string = row.find_element(By.TAG_NAME, "a").get_attribute("href")
                id = id_string[-4:-1]
                self.director_cache.append(Director(firstname=firstname, lastname=lastname, id=id))
        return list(self.director_cache)

