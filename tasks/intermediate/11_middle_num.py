if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))
    z = int(input('z = '))
    if y < x < z or z < x < y:
        print('x')
    elif x < y < z or z < y < x:
        print('y')
    else:
        print('z')
