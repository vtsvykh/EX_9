class User:
    """
    Class of the site user.

    Attributes:
        id (str):            user's unique number
        nick_name (str):     user's alias
        first_name (str):    name
        last_name (str):     surname
        middle_name (str):   patronymic
        gender (str):        gender
    """

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        """
        The function sets attributes for an instance of a class.
        :param id:           user's unique number
        :param nick_name:    user's alias
        :param first_name:   name
        :param last_name:    surname
        :param middle_name:  patronymic
        :param gender:       gender
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, **kwargs):
        """
        Function allows you to update data about the class instance.
        :param kwargs: user input data
        :return: updated user information
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __str__(self):
        """
        Outputs a string in a readable format.
        """
        return (f'User: {self.first_name} {self.middle_name} {self.last_name}, gender: {self.gender}, nickname: '
                f'{self.nick_name}, id: {self.id}')

    def __repr__(self):
        """
        Creates a string representation of an object.
        """
        return self.__str__


help(User)
