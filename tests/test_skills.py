from assertpy import assert_that


def test_displaying_list_of_skills(app):
    app.skills.open_skills_page_by_click()
    app.skills.get_list_of_skills()


def test_hide_skill_from_filter(app):
    app.offers.open_offers_page()
    old_list = app.skills.get_list_of_desired_skills()
    app.skills.hide_desired_skill()
    new_list = app.skills.get_list_of_desired_skills()
    assert old_list > new_list
    app.skills.find_hidden_skill()


def test_edit_skill(app):
    app.skills.open_skills_page()
    old_curr_value = app.skills.get_current_percentage_value()
    app.skills.edit_current_skill()
    old_desired_value = app.skills.get_desired_percentage_value()
    app.skills.edit_desired_skill()
    new_curr_value = app.skills.get_current_percentage_value()
    new_desired_value = app.skills.get_desired_percentage_value()
    assert_that(old_curr_value).is_not_equal_to(new_curr_value)
    assert_that(old_desired_value).is_not_equal_to(new_desired_value)


def test_add_skill_with_alphabet_list(app):
    app.skills.open_skills_page()
    old_list = app.skills.get_list_of_skills()
    app.skills.add_skill_from_alphabet_list()
    new_list = app.skills.get_list_of_skills()
    assert old_list < new_list


def test_delete_skill(app):
    app.skills.open_skills_page()
    old_list = app.skills.get_list_of_skills()
    if old_list <= 1:
        app.skills.add_skill_from_alphabet_list()
        app.skills.delete_skill()
        new_list = app.skills.get_list_of_skills()
        assert old_list > new_list
    else:
        app.skills.delete_skill()
        new_list = app.skills.get_list_of_skills()
        assert old_list > new_list


def test_add_skill_with_search_field(app):
    app.skills.open_skills_page()
    old_list = app.skills.get_list_of_skills()
    app.skills.transit_to_page_with_adding_skill()
    app.skills.add_skill_from_search_field()
    new_list = app.skills.get_list_of_skills()
    assert old_list < new_list
    app.skills.open_skills_page()
    app.skills.delete_skill()


def test_logout(app):
    app.session.logout()

