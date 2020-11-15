if __name__ == '__main__':
    a = int(input('min='))
    b = int(input('max='))
    c = int(input('step='))
    for i in range(a, b + 1, c):
        print(i, end=' ')

    print()
