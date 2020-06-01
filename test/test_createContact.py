# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="TestClient")] + [
    Group(name= random_string("contact", 10)) for i in range(3)
  ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_createContact(app, group):
       old_contacts = app.group.get_contact_list()
       app.group.create(group)
       assert len(old_contacts) + 1 == app.group.count()
       new_contacts = app.group.get_contact_list()
       old_contacts.append(group)
       assert old_contacts == new_contacts

