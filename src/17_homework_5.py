import math


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.r


if __name__ == '__main__':
    circle = Circle(10)
    area = circle.get_area()
    per = circle.get_perimeter()
    print(f'{area} and {per}')
