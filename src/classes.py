class character:
    max_speed = 100
    dead_health = 0
    TEMP = 10

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self._health = 100

    def hit(self, damage):
        self._health -= damage

    def is_dead(self):
        return self._health == self.dead_health

    @property
    def health(self):
        print("I am the 'x' property.")
        return self._health

    @health.setter
    def health_setter(self, value):
        self._health = value


class C:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print("I am the 'x' property.")
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class C1:
    def __init__(self, x):
        self._x = x

    def getx(self): return self._x

    def setx(self, value): self._x = value

    def delete_x(self): del self._x

    x = property(getx, setx, delete_x, "I'm the 'x' property.")


p = character("elf")
print(p._health)
p.hit(20)
print(p._health)
p.hit(80)
print(p.is_dead())
print(p.TEMP)
print("-----")
c = C(20)
print(c.x)
c.x = 10
print(c.x)
print("-----")
c1 = C1(20)
print(c1.x)
c1.x = 10
print(c1.x)