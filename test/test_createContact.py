# -*- coding: utf-8 -*-
from model.group import Group


def test_createContact(app):
  old_contacts = app.group.get_contact_list()
  contact = Group(name="TestContact")
  app.group.create(contact)
  assert len(old_contacts) + 1 == app.group.count()
  new_contacts = app.group.get_contact_list()
  old_contacts.append(contact)
  assert old_contacts == new_contacts

#def test_createContactClient(app):
#  old_contacts = app.group.get_contact_list()
#  contact = Group(name="TestClient")
#  app.group.create(contact)
#  new_contacts = app.group.get_contact_list()
#  assert len(old_contacts) + 1 == len(new_contacts)
#  old_contacts.append(contact)
#  assert sorted(old_contacts) == sorted(new_contacts)

