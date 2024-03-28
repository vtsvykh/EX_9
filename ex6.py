class Point:

    def __init__(self, crd=(0, 0)):
        self.x = crd[0]
        self.y = crd[1]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        dist = ((other.get_x() - self.x) ** 2 + (other.get_y() - self.y) ** 2) ** 0.5

        return dist

    def sum(self, other):
        new_crd = (self.x + other.get_x(), self.y + other.get_y())
        return new_crd

    def __str__(self):
        return f'({self.x}, {self.y})'
