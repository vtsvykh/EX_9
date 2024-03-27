class User:
    """

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
            self.attr = value

    def __str__(self):
        return f'Пользователь: {self.first_name} {self.last_name}, псевдоним: {self.nick_name}, id: {self.id}'

user1 = User(id=1, nick_name='user1', first_name='John', last_name='Doe')
print(user1)
user1.update(last_name='Smith', gender='male')
print(user1)