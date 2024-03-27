class User:
    """
    Class of site users.
    """

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __str__(self):
        return f'User: {self.first_name} {self.middle_name} {self.last_name}, gender: {self.gender}, nickname: {self.nick_name}, id: {self.id}'
