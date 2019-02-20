

class SignUp:
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return "%s;%s" % (self.name, self.email)

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email
