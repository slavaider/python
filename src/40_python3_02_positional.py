def avg(a, b, c, /, d):  # a,b,c position arguments
    return (a + b + c) / 3


def sum1(*, a, b):  # a,b keywards arguments
    return a + b


def sum2(a, b, /, *, c):  # a,b position arguments, c keyward argument
    return a + b + c


if __name__ == '__main__':
    x = float(3.2)
    print(x)
    print(avg(1, 2, 3, d=3))
    # print(avg(a=1, b=2, c=3)) error
    print(sum1(a=1, b=2))
    print(sum2(1, 2, c=3))
