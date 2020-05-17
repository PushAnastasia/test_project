from model.group import Group
from random import randrange

def test_inactive_some_contact(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_contacts = app.group.get_contact_list()
    index = randrange(len(old_contacts))
    app.group.inactive_contact_by_index(index)
    new_contacts = app.group.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts