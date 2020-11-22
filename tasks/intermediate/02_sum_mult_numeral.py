if __name__ == '__main__':
    x = input('x[3]=')
    x = [int(i) for i in x]
    res_sum = 0
    res_mul = 1
    for i in x:
        res_sum += i
        res_mul *= i
    print(f'{res_sum=},{res_mul=}')
