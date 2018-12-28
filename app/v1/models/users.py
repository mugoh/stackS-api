from werkzeug.security import generate_password_hash, check_password_hash

from base_model import BaseModel

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
        self.password = generate_password_hash(passw)

    def check_password(self, password_value):
        return check_password_hash(self.password, password_value)

    def save(self):
        users.append(self)

    def dictify(self):

        return {'username': self.username,
                'email': self.email,
                'password': self.password
                }

    def __repr__(self):
        return '{username} {email}'.format(
            self.dictify())

    @classmethod
    def get_by_name(cls, title):

        return [user for user in users
                if getattr(user, 'username') == title][0]

    @classmethod
    def get_by_id(cls, id):

        return [user for user in users
                if getattr(user, 'id') == id][0]