class Point:
    """
    Class of Point.
    """

    def __init__(self, crd=(0, 0)):
        """
        The function sets attributes for an instance of a class.
        """
        self.x = crd[0]
        self.y = crd[1]

    def get_x(self):
        """
        The function allows you to find out the x coordinate.
        """
        return self.x

    def get_y(self):
        """
        The function allows you to find out the y coordinate.
        """
        return self.y

    def distance(self, other):
        """
        The function allows you to find out the distance between points.
        """
        dist = ((other.get_x() - self.x) ** 2 + (other.get_y() - self.y) ** 2) ** 0.5

        return dist

    def sum(self, other):
        """
        The function allows you to find out the sum of two points.
        """
        new_crd = (self.x + other.get_x(), self.y + other.get_y())
        return new_crd

    def __str__(self):
        return f'({self.x}, {self.y})'

p = Point()
print(p)