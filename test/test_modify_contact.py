from model.group import Group

def test_modify_contact_name(app):
  old_contacts = app.group.get_contact_list()
  app.group.modify_first_contact(Group(name="ModifiedContact"))
  new_contacts = app.group.get_contact_list()
  assert len(old_contacts)  == len(new_contacts)