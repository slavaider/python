from typing import Literal, Final, final, Dict, TypedDict


def open_file(file, mode: Literal['r', 'rb', 'w', 'wb']):
    print(f'{file} open in mode {mode}')


open_file("lol.txt", "r")
f: Final = 3
f = 4
print(f)


@final
class d:
    def __init__(self):
        self.one = 1


class d1(d):
    def __init__(self):
        super().__init__()
        self.one = 1
        self.two = 2


d3 = d1()
print(d3.one)
print(d3.two)
person: Dict[str, any] = {"lol": 1, "lol1": "lol3"}


class word(TypedDict):
    comment: int
    word: str
    count: int


person1: word = {'comment': 3, 'word': "lol", 'count': 4}
