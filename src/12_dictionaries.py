from sortedcontainers import SortedDict


def sort_dictionary(dict):
    lst = list(dict.keys())
    lst = sorted([str(i) for i in lst])
    copy = {}
    for i in lst:
        copy[i] = dict[i]
    return copy


if __name__ == '__main__':
    # dictionaries and shit
    players = {"lol2": 123, "lol1": 456}
    players1 = dict(lol1=123, lol2=456, lol0=1)
    print(players["lol1"])
    print(players1.get('lol1'))
    players1[-1] = 2
    print(f'{players=}')
    players = dict(SortedDict(players))
    print(f'{players=}')
    print()
    print(f'{players1=}')
    del players1[-1]
    print("lol1" in players1)
    print("lol1" not in players1)
    print('print dictionary')
    for k, v in players1.items():
        print(k, v)
