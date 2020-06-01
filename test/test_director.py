
def test_data_on_edit_director_page(app):
    director_from_directors_page = app.director.get_director_list()[1]
    director_from_edit_page = app.director.get_director_info_from_edit_page(1)
    assert director_from_directors_page.fullname_from_directrors_page == merge_names_like_on_directors_page(director_from_edit_page)

def merge_names_like_on_directors_page(director):
    return " ".join([director.firstname, director.lastname])
