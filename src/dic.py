players = {"lol1": 123, "lol2": 456}
players1 = dict(lol1=123, lol2=456, lol0=1)
print(players["lol1"])
print(players1.get('lol1'))
players1[-1] = 2
players1
del players1[-1]
list(players1.keys())
sorted([players1.keys()])
print("lol1" in players1)
print("lol1" not in players1)
for k, v in players1.items():
    print(k, v)
