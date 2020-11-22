if __name__ == '__main__':
    x = int(input('x='))
    print('Количество разрядов:', len(str(abs(x))))
    res_sum = 0
    while x != 0:
        res_sum += 1
        x //= 10
    print(res_sum)

