from collections import namedtuple

if __name__ == '__main__':
    # namedtuple
    k = ('1', '2', '3')
    k1 = namedtuple("k1", "name age best_time")
    k2 = [k1("1", "2", "3"), k1("1", "2", "3"), k1("1", "2", "3")]
    for i in range(len(k2)):
        print(f"name {k2[i].name},age {k2[i].age},rating {k2[i].best_time}")

    time = namedtuple('time', 'best_time')
    total = [time(best_time=15)]
    print(total[0].best_time)
