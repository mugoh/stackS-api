from base_model import BaseModel

users = []  # Hold all user records


class UserModel(BaseModel):

    def __init__(self, username, email, password):

        super().__init__(users)
        self.email = email
        self.username = username
        self.password = password

    def save(self):
        users.append(self.dictify())

    @classmethod
    def get_by_name(cls, title):

        return [user for user in users
                if user['username'] == title][0]

    @classmethod
    def get_by_id(cls, id):

        return [user for user in users
                if user['id'] == id][0]

    def dictify(self):

        return {'username': self.username,
                'email': self.email,
                'password': self.password
                }
