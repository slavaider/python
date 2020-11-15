if __name__ == '__main__':
    a = int(input('a='))
    b = int(input('b='))
    a, b = b, a
    print(f'{a=},{b=}')
