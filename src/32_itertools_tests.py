import itertools as it


def print_iterables(iterable, end=None):
    for i in iterable:
        if end:
            print(i, end=end)
        else:
            print(i)
    print("\n")


def search_max(a, b):
    if a > b:
        return a
    elif b > a:
        return b


if __name__ == '__main__':
    i1 = iter([1, 2, 3])
    print(type(i1))
    print(next(i1))
    print()

    even_nums = [x for x in range(10) if x % 2 == 0]
    print(even_nums)
    even_nums1 = it.count(0, 2)  # itertools.count
    print([next(even_nums1) for _ in range(5)])
    print()

    print(list(zip(it.count(), ["a", "b", "c"])))
    ones = it.repeat(1, 5)  # itertools.repeat
    print_iterables(ones, ":")
    print(list(map(pow, range(10), it.repeat(2))))
    peg_ones = it.cycle([1, -1])
    print(list(next(peg_ones) for _ in range(10)))
    print(list(it.accumulate([1, 2, 3, 4, 5])))  # itertools.accumulate fib?
    print(list(it.accumulate(["A", "B", "C", "D"])))
    print(list(it.accumulate([3, 4, 3, 10, 5], max)))
    print(list(it.chain("ABC", "DEF")))
    print(list(it.chain.from_iterable(["ABC", "DEF"])))
    print(sorted(list(it.chain([1, 32], [2, 2, 5, 67], [2, 3, 5, 6]))))
    print(list(it.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5, 6])))  # itertools.dropwhile
    print(list(it.takewhile(lambda x: x < 3, [1, 2, 3, 4, 5, 6])))  # itertools.takewhile
    print(list(it.filterfalse(lambda x: x % 2 == 0, range(10))))  # itertools.filterfalse
    print()

    players = ["p1", "p2", "p3", "p4"]
    ratings = [1, 2, 3]
    # for p, r in zip(players, ratings):
    #     print(f"player {p} has {r} rating")
    print(dict(zip(players, ratings)))
    print(dict(it.zip_longest(players, ratings, fillvalue=0)))  # itertools.zip_longest
    print()

    for key, gp in it.groupby(sorted([1, 1, 1, 1, 2, 23, 3, 4, 5, 1])):  # itertools.groupby
        print(f"{key}:{list(gp)}")
    print()

    print(list(it.islice(it.count(0, 2), 0, 10)))
    print(list(it.islice(it.count(0, 2), 2, 10, 2)))
    print()

    pin = [7, 5, 2, 8]
    print(list(it.permutations(pin)))  # easy passwords
    print()

    ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["H", "D", "C", "S"]
    print(list(it.product(ranks, suits)))  # combine ranks and suits
    print(list(it.combinations("ABCD", 2)))  # combine 'ABCD' by 2 words
    print(list(it.combinations_with_replacement("ABCD", 2)))  # combine 'ABCD' by 2 with replacement
