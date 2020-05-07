# -*- coding: utf-8 -*-
from model.group import Group


def test_createContact(app):
  app.session.login(username="test0001push@gmail.com", password="plokijuh1")
  app.group.create(Group(name="TestContact"))

def test_createContactClient(app):
  app.session.login(username="test0001push@gmail.com", password="plokijuh1")
  app.group.create(Group(name="TestClient"))

