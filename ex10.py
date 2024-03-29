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


class Segment:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.one_intersection = False
class CoordinateSystem:
    segments = []

    @classmethod
    def add_segments(cls, segment):
        CoordinateSystem.segments.append(segment)

    def axis_intersection(self):
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count


point_1 = Point((1, 2))
point_2 = Point((3, 2))
segment1 = Segment(point_1, point_2)
print(Segment)
segment1.one_intersection = True

point3 = Point((0, 0))
point4 = Point((0, 4))
segment2 = Segment(point3, point4)
segment2.one_intersection = False

coordinate_system = CoordinateSystem()
coordinate_system.add_segments(segment1)
coordinate_system.add_segments(segment2)

print(coordinate_system.axis_intersection())  # Вывод: 1
