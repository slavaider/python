if __name__ == '__main__':
    print("hello".rjust(10) + '!')
    print("hello".ljust(10) + '!')
    print("hello".center(10) + '!')
    print(f"%1.2f" % 3.141593)
    a = 3
    b = 1
    c = 10
    print(max([a, b, c]))
    print()

    # y = 2x - 10, если x > 0
    # y = 0, если x = 0
    # y = 2 * |x| - 1, если x < 0
    x = int(input('x='))
    if x > 0:
        y = 2 * x - 10
    elif x == 0:
        y = 0
    else:
        y = 2 * abs(x) - 1
    print(y)


