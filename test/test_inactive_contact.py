from model.group import Group

def test_inactive_first_contact(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.inactive_first_contact()