import pytest
from data.signup import *


@pytest.mark.usefixtures('stop_2')
@pytest.mark.parametrize("email", email, ids=[repr(x) for x in email])
@pytest.mark.parametrize("name", name, ids=[repr(x) for x in name])
def test_signup_with_interrupting(signup, name, email):
    signup.sign_up.start_signup()
    signup.sign_up.fill_out_form(name, email)
    signup.sign_up.transfer_to_mailbox(mailbox)
    signup.sign_up.specify_login_password(mail_login, mail_password)
    signup.sign_up.confirm_email_and_transfer_to_account()
    signup.sign_up.check_users_account()


@pytest.mark.usefixtures('stop_2')
@pytest.mark.parametrize("email_cv", email_cv, ids=[repr(x) for x in email])
@pytest.mark.parametrize("name_cv", name_cv, ids=[repr(x) for x in name])
def test_signup_with_cv(signup, name_cv, email_cv):
    signup.sign_up.start_signup()
    signup.sign_up.fill_out_form(name_cv, email_cv)
    signup.sign_up.choice_all_options()
    signup.sign_up.get_confirmation_message()
    signup.sign_up.transfer_to_mailbox(mailbox)
    signup.sign_up.specify_login_password(mail_login, mail_password)
    signup.sign_up.confirm_email_and_transfer_to_account()
    signup.sign_up.check_users_account()


@pytest.mark.usefixtures('stop_2')
@pytest.mark.parametrize("email_zero", email_zero, ids=[repr(x) for x in email])
@pytest.mark.parametrize("name_zero", name_zero, ids=[repr(x) for x in name])
def test_signup_zero_character(signup_invite, name_zero, email_zero):
    signup_invite.sign_up.start_signup()
    signup_invite.sign_up.fill_out_form(name_zero, email_zero)
    signup_invite.sign_up.choose_zero_character()
    signup_invite.sign_up.transfer_to_mailbox(mailbox)
    signup_invite.sign_up.specify_login_password(mail_login, mail_password)
    signup_invite.sign_up.confirm_email_and_transfer_to_account()
    signup_invite.sign_up.check_users_account()


@pytest.mark.usefixtures('stop_2')
@pytest.mark.parametrize("email_link", email_link, ids=[repr(x) for x in email])
@pytest.mark.parametrize("name_link", name_link, ids=[repr(x) for x in name])
def test_signup_with_invitation_link(signup_invite, email_link, name_link):
    signup_invite.sign_up.start_signup()
    signup_invite.sign_up.fill_out_form(name_link, email_link)
    signup_invite.sign_up.choice_all_options()
    signup_invite.sign_up.get_confirmation_message()
    signup_invite.sign_up.transfer_to_mailbox(mailbox)
    signup_invite.sign_up.specify_login_password(mail_login, mail_password)
    signup_invite.sign_up.confirm_email_and_transfer_to_account()
    signup_invite.sign_up.check_users_account()


@pytest.mark.usefixtures('stop_2')
@pytest.mark.parametrize("email_del", email_del, ids=[repr(x) for x in email])
@pytest.mark.parametrize("name_del", name_del, ids=[repr(x) for x in name])
def test_delete_user(signup, name_del, email_del):
    signup.sign_up.start_signup()
    signup.sign_up.fill_out_form(name_del, email_del)
    signup.sign_up.transfer_to_mailbox(mailbox)
    signup.sign_up.specify_login_password(mail_login, mail_password)
    signup.sign_up.confirm_email_and_transfer_to_account()
    signup.sign_up.check_users_account()
    signup.profile.delete_user()
