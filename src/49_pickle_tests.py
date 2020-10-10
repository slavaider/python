import pickle


class Character:
    def __init__(self, race, armor, damage=10):
        self.armor = armor
        self.race = race
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

    def __setstate__(self, state):
        self.race = state.get('race', 'elf')
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 20)
        self.health = state.get('health', 100)


if __name__ == '__main__':
    # pickle or binary serialisation
    c = Character("elf", 10)
    with open(r'C:\Users\User\PycharmProjects\first_project\files\test.bin', "w+b") as file:
        pickle.dump(c, file)
    with open(r'C:\Users\User\PycharmProjects\first_project\files\test.bin', "r+b") as file:
        c = pickle.load(file)
    print(c.__dict__)
