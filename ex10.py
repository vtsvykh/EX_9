class Point:
    """
    Class of Point.
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
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()


class Segment:
    """
    Class of segment.
    """
    one_intersection = False

    def __init__(self, point_1, point_2):
        """
        The function sets attributes for an instance of a class.
        :param point_1: coordinates of the first point
        :param point_2: coordinates of the second point
        """
        self.point_1 = point_1
        self.point_2 = point_2
        self.segment = (point_1, point_2)

    def __str__(self):
        return f'{self.segment}'


class CoordinateSystem:
    """
    Class of Coordinate System.
    """
    segments = []

    @classmethod
    def add_segments(cls, segment):
        """
        the function adds a segment to the plane
        :param segment: coordinates of the extreme points of the segment
        """
        CoordinateSystem.segments.append(segment)

    def axis_intersection(self):
        """
        the function finds the number of intersections
        :return: number of intersections
        """
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count
