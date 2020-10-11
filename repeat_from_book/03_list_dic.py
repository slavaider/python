if __name__ == '__main__':
    x = [1, 2, 3]
    print('Списки')
    # list[start:end:step] default list[0==' ', max_length==' ', 1==' ']
    print(x[0:])
    print(x[1:])
    print(x[2:])
    print(x[:0])
    print(x[:1])
    print(x[:2])
    print(x[-1])
    print(x[-2:])
    print('Словари')
    y = {1: 2, 3: 4, 5: 6}
    print(y[1])
    print('vowels')
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = 'Milliways'
    res = []
    res.extend([1])
    print(res)
    temp = res.pop(0)
    res.append(temp)
    print(res)
    res.remove(temp)
    res.insert(0, temp)
    print(res)
    res.insert(1, 'lol')
    print(res)
    res.pop()
    res.pop()
    for i in word:
        if (i in vowels) and (i not in res):
            res.append(i)
    print(res)
