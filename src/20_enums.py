from enum import Enum
from enum import IntEnum
from enum import IntFlag


class Traffic(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Color(IntFlag):
    RED = 1
    GREEN = 2
    BLUE = 4


class Planets(Enum):
    MERCURY = (3.3e18, 2.4)
    EARTH = (5.4e20, 3.1)

    def __init__(self, mass, radius):
        self.radius = radius
        self.mass = mass

    @property
    def surface_gravity(self):
        g = 6.6
        return g * self.mass / (self.radius ** 2)


if __name__ == '__main__':
    print(Traffic.RED.name)
    print(Traffic.RED.value)
    for c in Traffic:
        print(c)
    print(Traffic(1))
    print(Traffic['RED'])
    print(Priority.LOW < Priority.HIGH)
    combination = Color.RED | Color.GREEN
    print(combination)
    print(Color.RED in combination)
    print(Planets.EARTH.value)
    print(Planets.EARTH.surface_gravity)
