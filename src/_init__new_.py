class Character:
    
    _instance = None

    def __new__(cls):
        if not cls._instance:
            print("create_class")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = "elf"


c = Character()
print(c.race)
c1 = Character()
print(c1.race)

c1.race = "ork"
print(f'{c.race} {c1.race} WOT?')
