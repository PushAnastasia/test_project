# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import unittest
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture

def test_createContact(app):
  app.session.login(username="test0001push@gmail.com", password="plokijuh1")
  app.group.create(Group(name="TestContact"))

def test_createContactClient(app):
  app.session.login(username="test0001push@gmail.com", password="plokijuh1")
  app.group.create(Group(name="TestClient"))

