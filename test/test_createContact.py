# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_contact import constant as testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_createContact(app, group):
       old_contacts = app.group.get_contact_list()
       app.group.create(group)
       assert len(old_contacts) + 1 == app.group.count()
       new_contacts = app.group.get_contact_list()
       old_contacts.append(group)
       assert old_contacts == new_contacts

