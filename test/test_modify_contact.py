from model.group import Group

def test_modify_contact_name(app):
  old_contacts = app.group.get_contact_list()
  contact = Group(name="ModifiedContact")
  app.group.modify_first_contact(contact)
  new_contacts = app.group.get_contact_list()
  assert len(old_contacts)  == len(new_contacts)
  old_contacts[0] = contact
  assert old_contacts == new_contacts