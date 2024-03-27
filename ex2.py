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
        self.num_sheep = 0

    def add_sheep(self, num_sheep):
        """
        Method allows you to add sheep to the sheep counter.
        :param num_sheep: number of sheep counted
        """
        self.num_sheep += num_sheep

    def __str__(self):
        return f'{self.name}, {self.num_sheep}'

    def __repr__(self):
        return self.__str__


boy = NotSleeping('Vasya')
boy.add_sheep(10)
