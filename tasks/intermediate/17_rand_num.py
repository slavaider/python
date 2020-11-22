import random

if __name__ == '__main__':
    x = random.randint(0, 100)
    tries = 10
    print(x)
    while tries > 0:
        print(f'{tries=}')
        answer = int(input('choice = '))
        if x == answer:
            print('You won')
            break
        elif answer > x:
            print('You choice is bigger')
            tries -= 1
        elif answer < x:
            print('You choice is lower')
            tries -= 1
