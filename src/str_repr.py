# repr eq neq training
from datetime import datetime

lst = [1, 2, 3]
print(lst)
s = repr(lst)
print(eval(s) == lst)
dt = datetime.today()
print(repr(dt))
print(dt)


class Character:
    def __init__(self, race, armor=10):
        self.race = race
        self.armor = armor

    def __repr__(self):
        return f"Character('{self.race}', {self.armor})"

    def __str__(self):
        return f'{self.race} and {self.armor}'

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.armor == other.armor
        return False

    def __neg__(self):
        pass


c = Character('elf')
d = eval(repr(c))
print(repr(c))
print(c == d)
