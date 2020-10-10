from typing import Protocol, List


class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:
    def swim(self):
        print("swim with hands")


class Flies(Protocol):
    def fly(self): ...


def process_flies(flies: List[Flies]):
    for i in flies:
        try:
            i.fly()
        except Exception as ex:
            print(repr(ex))


if __name__ == '__main__':
    process_flies([Bird(), Airplane(), Fish()])
