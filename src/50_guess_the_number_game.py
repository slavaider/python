import random

if __name__ == '__main__':
    # random module test
    r = random.randint(0, 10)
    tries = 0
    print("Игра 'Угадай число' у вас есть 6 попыток на отгадку")
    while tries < 6:
        n = int(input("Введите число = "))
        if n < r:
            print(f"Загаданное число больше,число попыток = {5 - tries}")
        elif n > r:
            print(f"Загаданное число меньше,число попыток = {5 - tries}")
        else:
            tries = -1
            break
        tries += 1
    if tries == -1:
        print(f"Число {r} отгадано")
    else:
        print(f"Число {r} не отгадано")
