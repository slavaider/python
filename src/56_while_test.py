if __name__ == '__main__':
    # Сумма всех нечётных чисел от 1 до 11 не превышающая 10
    values = list(range(1, 11))
    total_sum = 0
    for v in values:
        if v % 2 == 0:
            continue
        else:
            total_sum += v
            if total_sum > 10:
                break
    print(total_sum)
