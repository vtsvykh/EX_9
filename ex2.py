class NotSleeping:
    """
    Class of the falling asleep person.

    Attributes:
        name (str): name of the class instance
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
        """
        Outputs a string in a readable format.
        """
        return f'{self.name}, {self.__num_sheep}'

    def __repr__(self):
        """
        Creates a string representation of an object.
        """
        return self.__str__()
