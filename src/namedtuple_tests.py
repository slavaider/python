# namedtuple
from collections import namedtuple

k = ('1', '2', '3')
k1 = namedtuple("k1", "name age best_time")
k2 = [k1("1", "2", "3"), k1("1", "2", "3"), k1("1", "2", "3")]
for i in range(len(k2)):
    print(f"name {k2[i].name},age {k2[i].age},rating {k2[i].rating}")

time = namedtuple('time','best time')
total = [time(15)]

time = namedtuple('time','best_time')
total = [time(15)]

