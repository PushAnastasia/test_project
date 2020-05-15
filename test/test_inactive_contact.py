from model.group import Group

def test_inactive_first_contact(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_contacts = app.group.get_contact_list()
    app.group.inactive_first_contact()
    new_contacts = app.group.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts