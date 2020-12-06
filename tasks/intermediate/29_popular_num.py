import random

if __name__ == '__main__':
    rand_list = [random.randint(1, 5) for _ in range(10)]
    popular = 0
    num = 0
    for i in rand_list:
        temp = rand_list.count(i)
        if temp > popular:
            popular = temp
            num = i
    print(rand_list)
    print(popular, 'раз(а) встречается число', num)
