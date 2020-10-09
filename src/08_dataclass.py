from dataclasses import dataclass


@dataclass()
class DataClass:
    isTrue: bool
    data: int
    name: str


if __name__ == '__main__':
    # data class like interface
    d = DataClass(True, 10, "lol")
    print(d.data)
