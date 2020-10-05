# task 1
n = int(input("Введите строки = "))
i = 1
while i < n+1:
    print(f"{'*'*i}")
    i += 1
# task 2
n1 = int(input("Введите число = "))
for i in range(n1 + 1):
    if i % 2 == 1:
        print(f"{i} ODD")
    else:
        print(f"{i} EVEN")
# task 3
current_hand = [2, 3, 4, 10, 'Q', 5]
d = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0,
     9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
cards_sum = 0
for i in range(len(current_hand)):
    cards_sum += d[current_hand[i]]
print(cards_sum)
