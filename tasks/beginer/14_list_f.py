if __name__ == '__main__':
    list1 = [float(input('x=')) for _ in range(3)]
    s = 0
    m = 1
    for i in list1:
        s += i
        m *= i
    print(list1, f'{s=}', f'{m=}')
