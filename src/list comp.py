# list comprehension
s = "hello world"
chars = []
for char in s:
    chars.append(char)
print(chars)
chars1 = list(s)
print(chars1)
chars2 = [i for i in s]
print(chars2)
n = [n * n for n in range(1, 11)]
print(n)
n2 = [n * n for n in range(1, 11) if n % 2 == 0]
print(n2)
l1 = [2, 4, -5, 6, 8, -2]
l2 = [2, -6, 8, 3, 5, -2]
l3 = [(i, k) for i in l1 for k in l2 if i + k == 0]
print(l3)
