s = set({1, 2, 3})
print(type(s))
print(s)
s.add(2)
l1 = [1, 1, 1, 2, 3, 4, 5]
s = set(l1)
s.clear()
s1 = {1, 2, 3, 4, 6}
s2 = {1, 2, 3, 4, 5}
# подмножество
s1.issubset(s2)
# надмножество
s2.issuperset(s1)
# объединение s1+s2
s3 = s1.union(s2)
print(s3)
# пересечение ||
s4 = s1.intersection(s2)
print(s4)
# &&
s5 = s1.symmetric_difference(s2)
print(s5)
# update union without s3
s1.update(s2)
print(s1)
s1.remove(1)
s1.discard(2)
print(s1.pop())
