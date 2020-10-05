# Использование type hints
from typing import Optional


class Character:
    def __init__(self, power: int, armor: int):
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_live(self):
        return self.health > 0


c = Character(10, 10)
print(c.is_live())
type1 = Optional[int]
type1 = 10
type1 = "123"
print(type1)
