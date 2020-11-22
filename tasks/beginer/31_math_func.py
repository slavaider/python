if __name__ == '__main__':
    # y = x**2 при -5 <= x <= 5;
    # y = 2*|x|-1 при x < -5;
    # y = 2x при x > 5.
    def func(value):
        if -5 <= value <= 5:
            return value ** 2
        elif value < 5:
            return 2 * abs(value) - 1
        else:
            return 2 * value


    for x in range(-10, 11):
        print(func(x), end=' ')
