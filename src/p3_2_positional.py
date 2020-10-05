x = float(3.2)
print(x)


def avg(a, b, c, /, d):  # position arguments
    return (a + b + c) / 3


def sum1(*, a, b):  # keyward arguments
    return a + b


def sum2(a, b, /, *, c):
    return a + b + c


print(avg(1, 2, 3, d=3))
# print(avg(a=1, b=2, c=3))
print(sum1(a=1, b=2))
print(sum2(1, 2, c=3))
