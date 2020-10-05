print(walrus := True)
print(type(walrus))

# rows = int(input("rows = "))
# for i in range(rows):
#     print("*" * (i+1))

for i in range(rows := int(input("rows = "))):
    print("*" * (i + 1))

test = None
if mode := test:
    print(1)
