class Dog:
    """
    Class of dog.
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
        :return:
        """
        print('Гав!')

    def __str__(self):
        return f'Собака: {self.name}'

    def __repr__(self):
        return self.__str__()


puppy = Dog('Барбос')
puppy.say()
