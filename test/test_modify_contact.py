from model.group import Group

def test_modify_contact_name(app):
  app.session.login(username="test0001push@gmail.com", password="plokijuh1")
  app.group.modify_first_contact(Group(name="New Contact"))