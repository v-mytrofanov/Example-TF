

def test_displaying_offers_and_review_full_list(app):
    app.offers.open_offers_page_by_click()
    app.offers.review_all_courses()


def test_choose_course_as_favorite(app):
    app.offers.open_favorite_offers_page()
    old_list = app.offers.get_list_of_favorite_courses()
    app.offers.open_offers_page_by_click()
    app.offers.select_any_course_as_favorite()
    app.offers.open_favorite_offers_page()
    new_list = app.offers.get_list_of_favorite_courses()
    assert old_list < new_list


def test_delete_favorite_course_from_favorites_courses(app):
    app.offers.open_favorite_offers_page()
    if app.offers.get_list_of_favorite_courses() == 0:
        app.offers.open_offers_page_by_click()
        app.offers.select_any_course_as_favorite()
        app.offers.open_favorite_offers_page()
        old_list = app.offers.get_list_of_favorite_courses()
        app.offers.delete_favorite_course()
        new_list = app.offers.get_list_of_favorite_courses()
        assert old_list > new_list
    else:
        old_list = app.offers.get_list_of_favorite_courses()
        app.offers.delete_favorite_course()
        new_list = app.offers.get_list_of_favorite_courses()
        assert old_list > new_list


def test_choose_course_as_archived(app):
    app.offers.open_archived_offers_page()
    old_list = app.offers.get_list_of_all_courses()
    app.offers.open_offers_page_by_click()
    app.offers.select_first_course_as_archived()
    app.offers.open_archived_offers_page()
    new_list = app.offers.get_list_of_all_courses()
    assert old_list < new_list
    app.offers.get_title_archived_course_and_find_one_in_offers()


def test_delete_archived_course_from_archived_courses(app):
    app.offers.open_archived_offers_page()
    if app.offers.get_list_of_all_courses() == 0:
        app.offers.open_offers_page_by_click()
        app.offers.select_first_course_as_archived()
        app.offers.open_archived_offers_page()
        app.offers.get_title_of_course()
        old_list = app.offers.get_list_of_all_courses()
        app.offers.delete_archived_course()
        new_list = app.offers.get_list_of_all_courses()
        assert old_list > new_list
        app.offers.find_ex_archived_course()
    else:
        old_list = app.offers.get_list_of_all_courses()
        app.offers.get_title_of_course()
        app.offers.delete_archived_course()
        new_list = app.offers.get_list_of_all_courses()
        assert old_list > new_list
        app.offers.find_ex_archived_course()


def test_check_displaying_skills_in_course(app):
    app.offers.open_offers_page_by_click()
    app.offers.check_courses_skills()


def test_book_course(app):
    app.offers.open_offers_page_by_click()
    app.offers.choose_any_course()
    app.offers.mark_as_booked()
    app.offers.check_booked_course_on_page()


def test_cancel_booked_course(app):
    app.offers.open_booked_courses_page()
    if app.offers.get_list_of_all_courses() == 0:
        app.offers.open_offers_page_by_click()
        app.offers.choose_any_course()
        app.offers.mark_as_booked()
        app.offers.check_booked_course_on_page()
        old_list = app.offers.get_list_of_all_courses()
        app.offers.cancel_booking_course()
        app.offers.open_booked_courses_page()
        new_list = app.offers.get_list_of_all_courses()
        assert old_list > new_list
    else:
        old_list = app.offers.get_list_of_all_courses()
        app.offers.cancel_booking_course()
        app.offers.open_booked_courses_page()
        new_list = app.offers.get_list_of_all_courses()
        assert old_list > new_list
