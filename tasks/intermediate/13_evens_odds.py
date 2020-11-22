if __name__ == '__main__':
    x = input('x = ')
    x = [int(i) for i in x]
    even = 0
    odd = 0
    for i in x:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'{even=},{odd=}')
