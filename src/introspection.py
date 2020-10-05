# print(issubclass.__doc__)
# help(issubclass)


class Shape:
    pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


c = Circle(10)
print(issubclass(Circle, Shape))
print(isinstance(c, Circle))
print(isinstance(1, int))
print(callable(c))
if hasattr(c, "radius"):
    print(getattr(c, "radius"))
    setattr(c, "radius", 20)
    print(getattr(c, "radius"))
print(dir(Circle))
print(__name__)