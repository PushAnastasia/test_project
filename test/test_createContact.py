# -*- coding: utf-8 -*-
from model.group import Group


def test_createContact(app):
  old_contacts = app.group.get_contact_list()
  app.group.create(Group(name="TestContact"))
  new_contacts = app.group.get_contact_list()
  assert len(old_contacts) + 1 == len(new_contacts)

def test_createContactClient(app):
  app.group.create(Group(name="TestClient"))

