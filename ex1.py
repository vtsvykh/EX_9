class Dog:
    """
    Class of dog.

    Attributes:
        name (str): name of the class instance
    """

    def __init__(self, name):
        """
        The function sets attributes for an instance of a class.
        :param name: name of the class instance
        """
        self.name = name

    def say(self):
        """
        The method of the instance of the class that outputs the phrase.
        """
        print('Гав!')

    def __str__(self):
        """
        Outputs a string in a readable format.
        """

        return f'Собака: {self.name}'

    def __repr__(self):
        """
        Creates a string representation of an object.
        """
        return self.__str__()

help(Dog)