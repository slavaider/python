numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)

print('-')
n1 = range(1, 6)
print(n1)
for i in n1:
    print(i)
print('-')
for i in range(1, 6):
    if i % 2 == 0:
        print(i)
print('-')
n2 = [1, 5, 7, 8, 9]
for i, item in enumerate(n2):
    n2[i] *= 2
    print(item)
print(n2)

for _ in range(1, 5):
    print("A")

print('-')
t = [('1', 1), ('2', 2), ('3', 3)]
for (name, number) in t:
    print(name)
    print(number)

print('-')
d = dict(lol1=1, lol2=2)
for (i, v) in d.items():
    print(f'{i} is {v}')

print('-')
l1 = [2, 4, -5, 6, 8, -2]
l2 = [2, -6, 8, 3, 5, -2]
combinations = []
for i in l1:
    for k in l2:
        if i + k == 0:
            combinations.append((i, k))
            print(f'{i} and {k}')
print(combinations)
