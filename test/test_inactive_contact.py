

def test_inactive_first_contact(app):
  app.session.login(username="test0001push@gmail.com", password="plokijuh1")
  app.group.inactive_first_contact()