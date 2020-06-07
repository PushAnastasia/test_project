# -*- coding: utf-8 -*-
from model.group import Group



def test_createContact(app, data_contacts):
       group = data_contacts
       old_contacts = app.group.get_contact_list()
       app.group.create(group)
       assert len(old_contacts) + 1 == app.group.count()
       new_contacts = app.group.get_contact_list()
       old_contacts.append(group)
       assert old_contacts == new_contacts

