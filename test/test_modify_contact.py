from model.group import Group

def test_modify_contact_name(app):
  app.group.modify_first_contact(Group(name="New Contact3"))