from model.signup import SignUp
import random
import string


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits

    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_email(prefix, domain):
    random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                          for _ in range(10))

    return prefix + random_part + '@' + domain


name = [SignUp(name=random_name("user_", 15))]
email = [SignUp(email=random_email(prefix='kyiv_qa+', domain='ukr.net'))]

name_cv = [SignUp(name=random_name("user_cv", 15))]
email_cv = [SignUp(email=random_email(prefix='kyiv_qa+cv', domain='ukr.net'))]

name_zero = [SignUp(name=random_name("user_zero", 15))]
email_zero = [SignUp(email=random_email(prefix='kyiv_qa+zero', domain='ukr.net'))]

name_link = [SignUp(name=random_name("user_link", 15))]
email_link = [SignUp(email=random_email(prefix='kyiv_qa+link', domain='ukr.net'))]

name_del = [SignUp(name=random_name("user_del", 15))]
email_del = [SignUp(email=random_email(prefix='kyiv_qa+del', domain='ukr.net'))]

mailbox = "https://accounts.ukr.net/login"
mail_login = ""
mail_password = ""
