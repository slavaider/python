from typing import Literal, Final, final, Dict, TypedDict

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


@final
class d:
    def __init__(self):
        self.one = 1


class d1(d):
    def __init__(self):
        super().__init__()
        self.one = 1
        self.two = 2


class MyDict(TypedDict):
    comment: int
    word: str
    count: int


def open_file(file, mode: Literal['r', 'rb', 'w', 'wb']):
    print(f'{file} open in mode {mode}')


if __name__ == '__main__':
    open_file("lol.txt", 'r')
    f: Final = 3  # const?
    f = 4
    print(f)
    d3 = d1()
    print(d3.one)
    print(d3.two)
    person: Dict[str, any] = {"lol": 1, "lol1": "lol3"}
    person1: MyDict = {'comment': 3, 'word': "lol", 'count': 4}

    c = Character(10, 10)
    print(c.is_live())
    type1 = Optional[int]
    type1 = 10
    type1 = "123"
    print(type1)
