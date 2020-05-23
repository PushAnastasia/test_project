
def test_data_on_edit_director_page(app):
    director_from_directors_page = app.director.get_director_list()[1]
    director_from_edit_page = app.director.get_director_info_from_edit_page(1)
    assert director_from_directors_page.firstname == director_from_edit_page.firstname
    assert director_from_directors_page.lastname == director_from_edit_page.lastname
