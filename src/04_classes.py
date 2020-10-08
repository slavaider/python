class Character:
    max_speed = 100
    dead_health = 0
    TEMP = 10

    def __init__(self, race, damage=10, armor=20, health=100):
        self.race = race
        self.damage = damage
        self.armor = armor
        self._health = health

    def hit(self, damage):
        self._health -= damage

    def is_dead(self):
        return self._health == self.dead_health

    @property  # getter
    def health(self):
        return self._health

    @health.setter  # setter
    def health(self, value):
        self._health = value


class C:
    def __init__(self, x):
        self._x = x

    @property  # getter
    def x(self): return self._x

    @x.setter  # setter
    def x(self, value): self._x = value

    @x.deleter  # deleter
    def x(self): del self._x


class C1:
    def __init__(self, x):
        self._x = x

    def getx(self): return self._x  # getter

    def setx(self, value): self._x = value  # setter

    def delete_x(self): del self._x  # deleter

    x = property(getx, setx, delete_x, "I'm the 'x' property.")  # combiner - easy


if __name__ == '__main__':
    # getter, setter for class:Character
    print("getter, setter for class:Character")
    p = Character("elf")
    print(p.health)
    p.hit(20)
    print(p.health)
    p.hit(80)
    p.health = 100
    print(p.is_dead())
    print(p.TEMP)
    # getter, setter for class:C
    print("getter, setter for class:C")
    c = C(20)
    print(c.x)
    c.x = 10
    print(c.x)
    # getter, setter for class:C1
    print("getter, setter for class:C1")
    c1 = C1(20)
    print(c1.x)
    c1.x = 10
    print(c1.x)
