import json


class Tour:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data_cls):
        return cls(**json_data_cls)


class Chess:
    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data_cls):
        tournaments = list(map(Tour.from_json, json_data_cls['tournaments']))
        return cls(tournaments)


Tours = {
    'Aero': 2010,
    'Fide': 2000,
    'Some': 2011
}

json_data = json.dumps(Tours, indent=2)  # serialization
print(type(json_data))
print(json_data)
loaded = json.loads(json_data)  # deserialization
print(type(loaded))
print(loaded)
t1 = Tour('Aero', 2010)
t2 = Tour('Fibro', 2011)
t3 = Tour('Zeta', 2014)
json_data = json.dumps(t1.__dict__, indent=2)
print(json_data)
t = Tour(**json.loads(json_data))
print(t.__dict__)
chess = Chess([t1, t2, t3])
# json_data = json.dumps([i.__dict__ for i in chess.tournaments], indent=2)
json_data = json.dumps(chess, default=lambda obj: obj.__dict__, indent=2)
# print(json_data)
chesses = Chess.from_json(json.loads(json_data))
print(chesses.tournaments)
with open(r"C:\Users\User\PycharmProjects\first_project\files\json_tests.txt", "w") as file:
    json.dump(chess, file, default=lambda obj: obj.__dict__, indent=2)
with open(r"C:\Users\User\PycharmProjects\first_project\files\json_tests.txt", "r") as file:
    data = json.load(file)
    decoded = Chess.from_json(data)
    print("----")
    print(data)
    print(decoded.tournaments)
