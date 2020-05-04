# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import unittest
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture

def test_createContact(app):
  app.login(username="test0001push@gmail.com", password="plokijuh1")
  app.create_contact(Group(name="TestContact"))

def test_createContactClient(app):
  app.login(username="test0001push@gmail.com", password="plokijuh1")
  app.create_contact(Group(name="TestClient"))

