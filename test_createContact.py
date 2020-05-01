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
    self.driver.get("https://skyt.qa.sharp.nixdev.co/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "email-address").click()
    self.driver.find_element(By.ID, "email-address").send_keys("test0001push@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".loginWrap > .accountcontrol__content").click()
    self.driver.find_element(By.CSS_SELECTOR, ".loginWrap > .accountcontrol__content").send_keys("plokijuh1")
    self.driver.find_element(By.ID, "btnLogin").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".create-block .link-content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".create-block .link-content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Contact").click()
    self.driver.find_element(By.ID, "CompanyName").click()
    self.driver.find_element(By.ID, "CompanyName").send_keys("TestContact")
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > .grey-block").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-save").click()
  
