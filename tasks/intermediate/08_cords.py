if __name__ == '__main__':
    x = float(input('x = '))
    y = float(input('y = '))
    if x > 0 and y > 0:
        print('I')
    elif x < 0 and y > 0:
        print('II')
    elif x < 0 and y < 0:
        print('III')
    elif x > 0 and y < 0:
        print('IV')
