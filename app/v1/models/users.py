from werkzeug.security import generate_password_hash, check_password_hash

from .base_model import BaseModel

users = []  # Hold all user records


class UserModel(BaseModel):

    def __init__(self, username, email, password):

        super().__init__(users)
        self.email = email
        self.username = username
        self.password = password

    @property
    def password(self):
        return None

    @password.setter
    def password(self, passw):
        self._password = generate_password_hash(passw)

    def check_password(self, password_value):
        return check_password_hash(self._password, password_value)

    def save(self):
        users.append(self)

    def dictify(self):

        return {'username': self.username,
                'password': self.password,
                'email': self.email,
                }

    def __repr__(self):
        return '{username} {email}'.format(**
                                           self.dictify())

    @classmethod
    def get_by_name(cls, title):

        user = [user for user in users
                if getattr(user, 'username') == title]

        return user[0] if user else None

    @classmethod
    def get_by_email(cls, email):

        found_user = [user for user in users
                      if getattr(user, 'email') == email]

        return found_user[0] if found_user else None

    @classmethod
    def get_all_users(cls):
        return [user.dictify() for user in users]
