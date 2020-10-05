from dataclasses import dataclass


@dataclass()
class data_c:
    isTrue: bool
    data: int
    name: str


d = data_c(True, 10, "lol")
print(d.data)
