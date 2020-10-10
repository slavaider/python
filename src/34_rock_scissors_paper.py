import random

if __name__ == '__main__':
    dic = {1: "R", 2: "S", 3: "P"}
    trans = {'R': 'Rock', 'S': 'Scissors', 'P': 'Paper'}
    while True:
        # R/r-камень S/s-ножницы P/p-бумага
        print('R/r-камень S/s-ножницы P/p-бумага')
        g = input("Ваш выбор = ").lower()
        r = random.randint(1, 3)
        if g == dic[r].lower():
            print("Ничья")
        elif g == "r" and dic[r] == "P":
            print("Ты проиграл")
        elif g == "r" and dic[r] == "S":
            print("Ты выйграл")
        elif g == "s" and dic[r] == "R":
            print("Ты проиграл")
        elif g == "s" and dic[r] == "P":
            print("Ты выйграл")
        elif g == "p" and dic[r] == "R":
            print("Ты выйграл")
        elif g == "p" and dic[r] == "S":
            print("Ты проиграл")
        print(f"Выбор противника - {trans[dic[r]]}")
        print("Повторить? y/n")
        a = input()
        if a == 'y':
            continue
        elif a == 'n':
            break
