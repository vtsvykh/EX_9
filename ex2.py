class NotSleeping:
    """
    Class of the falling asleep person.
    """

    def __init__(self, name):
        """
        The function sets attributes for an instance of a class.
        :param name: name of the class instance
        """
        self.name = name
        self.__num_sheep = 0

    def add_sheep(self):
        """
        Method allows you to add sheep to the sheep counter.
        """
        self.__num_sheep += 1

    def __str__(self):
        return f'{self.name}, {self.__num_sheep}'

    def __repr__(self):
        return self.__str__
