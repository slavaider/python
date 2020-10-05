if __name__ == '__main__':

    vowels = ['o', 'a', 'i', 'u', 'e']
    word = input('Введите слово = ')
    found = {}
    for i in word:
        if i in vowels:
            found.setdefault(i, 0)
            found[i] += 1
    for k, v in sorted(found.items()):
        print('found word', k, ':', v, 'time(s)')
