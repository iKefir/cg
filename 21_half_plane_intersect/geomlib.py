from math import sqrt, fabs, inf
import matplotlib.pyplot as plt
from functools import total_ordering


@total_ordering
class Point(object):
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "Point(%s,%s)"%(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    def normalize(self):
        dist = sqrt(self.x ** 2 + self.y ** 2)
        return Point(self.x/dist, self.y/dist)
    
    def draw(self):
        plt.scatter(self.x, self.y)
    

class Line(object):
    # ax + by + c = 0
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c
        
    def point_from_line(self):
        if self.b != 0:
            return Point(0, -self.c/self.b)
        elif self.a != 0:
            return Point(-self.c/self.a, 0)
        else:
            return Point(0, 0)

    def get_tan(self):
        if self.b == 0:
            return inf if self.a <=0 else -inf
        return -self.a/self.b

    def get_point_for_x(self, x):
        if self.b == 0:
            if self.a == 0:
                return Point(0, 0)
            return Point(-self.c/self.a, x)
        return Point(x, (-self.c -self.a * x)/self.b)

    def get_two_infinite_points(self):
        if self.a == 0:
            return Point(-1000.0, -self.c/self.b), Point(1000.0, -self.c/self.b)
        if self.b == 0:
            return Point(-self.c/self.a, -1000.0), Point(-self.c/self.a, 1000.0)

        x1 = -1000.0; y1 = - (self.c + self.a * x1) / self.b
        x2 = 1000.0; y2 = - (self.c + self.a * x2) / self.b
        return Point(x1, y1), Point(x2, y2)

    def intersect(self, other):
        # Пересечение двух линий

        if other is None:
            return None

        det = self.a * other.b - self.b * other.a
        if det == 0:
            al_det = self.a * other.c - self.c * other.a
            if al_det == 0 and not (self.a == 0 and other.a == 0): # covariant or contrvariant
                return self.get_point_for_x(0)
            return None  # parallel

        x = (self.b * other.c - other.b * self.c) / det
        y = (other.a * self.c - self.a * other.c) / det

        return Point(x, y)

    def closest_point_to(self, point):
        # Ближайщая точка на прямой
        temp = self.a ** 2 + self.b ** 2
        bx0 = self.b * point.x
        ay0 = self.a * point.y
        x = (self.b * (bx0 - ay0) - self.a * self.c) / temp
        y = (self.a * (-bx0 + ay0)- self.b * self.c) / temp
        return Point(x, y)
    
    def normalize(self):
        if self.b != 0:
            m = -self.a/self.b
            b = -self.c/self.b
            return [m, b] 
        else:
            return [1, 0]

    def move(self, x, y):
        self.c = self.c+self.a*x+self.b*y

    def distance_to(self, point):
        return fabs(self.a * point.x + self.b * point.y + self.c ) / sqrt(self.a ** 2 + self.b ** 2)
    
    def draw(self, clr='black', lwidth=2.0, linestyle="-", alph=1.0, left_b = -15, right_b = 15):
        x1 = left_b
        x2 = right_b
        # ax + by + c = 0
        p1 = self.get_point_for_x(x1)
        p2 = self.get_point_for_x(x2)
        plt.plot((p1.x, p2.x), (p1.y, p2.y), 'k-', color=clr, linewidth=lwidth, linestyle = linestyle, alpha = alph)

    @staticmethod
    def from_point_dir(point, direction):
        if direction.x == 0:
            return Line(1, 0, -point.x)
        elif direction.y == 0:
            return Line(0, 1, -point.y)

        slope = direction.y / direction.x
        b = -1
        c = point.y - slope * point.x
        return Line(slope, b, c)

    @staticmethod
    def from_two_points(p_a, p_b):
        a = p_b.y - p_a.y
        b = p_a.x - p_b.x
        c = -(a * p_a.x +b * p_a.y)
        return Line(a, b, c)


class HalfPlane(Line):
    # ax + by + c <= 0
    def __init__(self, a, b, c):
        Line.__init__(self, a, b, c)

    def __contains__(self, point):
        return self.a * point.x + self.b * point.y + self.c <= 0.000001

    def __repr__(self):
        return "HP(a:%s b:%s c:%s)" % (self.a, self.b, self.c)

    def __str__(self):
        return "Halfplane(%s,%s,%s)" % (self.a, self.b, self.c)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def opposite(self):
        return HalfPlane(self.a * -1.0, self.b * -1.0, self.c * -1.0)

    # def move(self, x, y):
    #     super().move(x, y)

    def orientation_downright(self):
        # ax + by + c = 0
        # 0 0 - ld l
        # 0 1 - ld r
        # 1 0 - lu r
        # 1 1 - lu l
        if self.a != 0 and self.b != 0:
            x2 = 1
            y1 = -self.c / self.b
            right_point = Point(x2, y1)
            return right_point in self
        elif self.a != 0:
            e_point = self.point_from_line()
            return Point(e_point.x + 1, e_point.y) in self
        elif self.b != 0:
            e_point = self.point_from_line()
            return Point(e_point.x, e_point.y - 1) in self
        else:
            return False

    def intersect(self, other):
        if other is None:
            return None

        intersection = super().intersect(other)

        return intersection

    def intersect_from_point(self, point, other):
        intersection = super(HalfPlane, self).intersect(other)
        if intersection is not None and (intersection.y > point.y or (intersection.y == point.y and intersection.x < point.x)):
            return None
        return intersection
            
    def getDirection(self):
        return Point(self.a, self.b).normalize()

    def draw(self, bclr = 'black', clr='gray', lwidth = 9, alph = 0.5, left_b = -15, right_b = 15):
        const = 2.5 * 30/(right_b - left_b)
        direction = self.getDirection()
        direction = Point(-direction.x, -direction.y)
        p1 = self.get_point_for_x(left_b)
        p2 = self.get_point_for_x(right_b)
        p1 = Point(p1.x + direction.x/const, p1.y + direction.y/const)
        p2 = Point(p2.x + direction.x/const, p2.y + direction.y/const)
        l = Line.from_two_points(p1, p2)
        l.draw(clr, lwidth, "-", alph, left_b, right_b)
        super().draw(clr = bclr, left_b = left_b, right_b = right_b)
    

    @staticmethod
    def FromLineDir(line, direction):
        # На вход линия и вектор направления, на выход - полуплоскость
        point = None
        if line.b != 0:
            y = - line.c / line.b
            point = Point(0, y)
        else:
            x = - line.c / line.a
            point = Point(x, 0)

        shift = Point(point.x + direction.x, point.y + direction.y)

        if line.a * shift.x + line.b * shift.y + line.c <= 0:
            return HalfPlane(line.a, line.b, line.c)
        else:
            return HalfPlane(-line.a, -line.b, -line.c)