if __name__ == '__main__':
    # vowels = {'a', 'e', 'i', 'o', 'u'} alternate
    vowels = set('aeiou')
    word = 'hello'
    u = sorted(vowels.union(set(word)))
    print(u)
    d = sorted(vowels.difference(set(word)))
    print(d)
    i = sorted(vowels.intersection(set(word)))
    print(i)
