import math


class Pizza:
    _order = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self._order = Pizza._order
        Pizza._order += 1

    @property
    def order_number(self):
        return self._order

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])


p1 = Pizza.meat_festival()
p2 = Pizza.garden_feast()
p3 = Pizza.meat_festival()
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
