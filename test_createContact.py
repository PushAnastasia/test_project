# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestCreateContact():
  def setup_method(self, method):
    self.driver = webdriver.Chrome('C:\Program Files\Chromedriver\chromedriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createContact(self):
    self.open_home_page()
    self.login(username="test0001push@gmail.com", password="plokijuh1")
    self.open_add_contact_page()
    self.create_contact(name="TestContact")

  def create_contact(self, name):
    # fill Contact form
    self.driver.find_element(By.ID, "CompanyName").click()
    self.driver.find_element(By.ID, "CompanyName").send_keys(name)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > .grey-block").click()
    # submit creation
    self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()

  def open_add_contact_page(self):
    self.driver.find_element(By.CSS_SELECTOR, ".create-block .link-content").click()
    self.driver.find_element(By.LINK_TEXT, "Contact").click()

  def login(self, username, password):

    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "email-address").click()
    self.driver.find_element(By.ID, "email-address").send_keys(username)
    self.driver.find_element(By.ID, "cpassword").click()
    self.driver.find_element(By.ID, "cpassword").send_keys(password)
    self.driver.find_element(By.ID, "btnLogin").click()

  def open_home_page(self):

    self.driver.get("https://skyt.qa.sharp.nixdev.co/")
    self.driver.set_window_size(1936, 1056)
  
