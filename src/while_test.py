# Сумма всех нечётных чисел от 1 до 11 не превышающая 10
values = list(range(1, 11))
_sum = 0
for v in values:
    if v % 2 == 0:
        continue
    else:
        _sum += v
        if _sum > 10:
            break
print(_sum)
