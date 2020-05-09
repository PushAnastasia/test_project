# -*- coding: utf-8 -*-
from model.group import Group


def test_createContact(app):
  app.group.create(Group(name="TestContact"))

def test_createContactClient(app):
  app.group.create(Group(name="TestClient"))

