from data.profile import *


def test_change_zip_code(app):
    app.profile.open_profile_page_via_menu()
    old_zip = app.profile.get_zip_code()
    app.profile.change_zip_code()
    new_zip = app.profile.get_zip_code()
    assert old_zip != new_zip


def test_upload_and_change_avatar(app):
    app.profile.open_profile_page()
    app.profile.upload_avatar()


def test_upload_cv(app):
    app.profile.open_profile_page()
    app.profile.upload_cv()


def test_change_password(app):
    app.profile.open_profile_page()
    app.profile.specify_password(new_password)
    app.session.logout()
    app.profile.login_with_new_password(new_password, email)
    app.profile.open_profile_page()
    app.profile.specify_password(old_password)
