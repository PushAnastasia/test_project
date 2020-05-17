from model.group import Group
from random import randrange

def test_modify_contact_name(app):
  if app.group.count() == 0:
    app.group.create(Group(name="TestClient"))
  old_contacts = app.group.get_contact_list()
  index = randrange(len(old_contacts))
  contact = Group(name="TestClient")
  app.group.modify_contact_by_index(index, contact)
  new_contacts = app.group.get_contact_list()
  assert len(old_contacts) == len(new_contacts)
  old_contacts[index] = contact
  assert old_contacts == new_contacts