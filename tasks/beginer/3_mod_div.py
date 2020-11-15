if __name__ == '__main__':
    a = int(input('a='))
    b = int(input('b='))
    if a % b == 0:
        print('Делятся')
    else:
        print('Не делятся', a % b)
    print(a // b)
