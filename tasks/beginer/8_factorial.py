if __name__ == '__main__':
    x = int(input('x='))
    f = 0
    if x > 0:
        f = 1
    for i in range(2, x + 1):
        f *= i
    print(f)
