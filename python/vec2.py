import math


class Vec2:

    def __init__(self, x, y=None):
        if type(x) in {int, float}:
            self.x = x
            self.y = y
        elif len(x) == 2:
            self.x = x[0]
            self.y = x[1]

    def __str__(self):
        return f"Vec ({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        assert isinstance(other, type(self))
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        assert isinstance(other, type(self))
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert isinstance(other, type(self))
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, fac):
        assert type(fac) in {int, float}
        return Vec2(self.x * fac, self.y * fac)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, fac):
        assert type(fac) in {int, float}
        return Vec2(self.x / fac, self.y / fac)

    def __neg__(self):
        return Vec2(self.x, self.y) * -1

    def __pow__(self, other, modulo=None):  # skalar product
        assert isinstance(other, type(self))
        return self.x * other.x + self.y * other.y

    def __rpow__(self, other):
        return self.__pow__(other)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        return self / self.length()

    @staticmethod
    def angle_cos(v1, v2):
        return v1.normalize() ** v2.normalize()

    def toArray(self):
        return [self.x, self.y]
