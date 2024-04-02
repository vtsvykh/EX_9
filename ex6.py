class Point:
    """
    Class of Point.

    Attributes:
        crd (tuple): coordinates of the point
    """

    def __init__(self, crd=(0, 0)):
        """
        The function sets attributes for an instance of a class.
        :param crd: coordinates of the point
        """
        self.x = crd[0]
        self.y = crd[1]

    def get_x(self):
        """
        The function allows you to find out the x coordinate.
        :return: the x coordinate
        """
        return self.x

    def get_y(self):
        """
        The function allows you to find out the y coordinate.
        :return: the y coordinate
        """
        return self.y

    def distance(self, other):
        """
        The function determines the distance between two points.
        :param other: coordinates of another point
        :return: distance between two points
        """
        dist = ((other.get_x() - self.x) ** 2 + (other.get_y() - self.y) ** 2) ** 0.5

        return dist

    def sum(self, other):
        """
        The function allows you to find out the sum of two points.
        :param other: coordinates of another point
        :return: the sum of the coordinates of two points
        """
        new_crd = (self.x + other.get_x(), self.y + other.get_y())

        return new_crd

    def __str__(self):
        """
        Outputs a string in a readable format.
        """
        return f'({self.x}, {self.y})'

    def __repr__(self):
        """
        Creates a string representation of an object.
        """
        return self.__str__()
