from collections import OrderedDict

d1 = dict(a='A', b='B', c='C')
d2 = dict(c='C', b='B', a='A')
print(d1 == d2)
d1 = OrderedDict(a='A', b='B', c='C')
d2 = OrderedDict(c='C', b='B', a='A')
print(d1 == d2)
