if __name__ == '__main__':
    print(walrus := True)
    print(type(walrus))

    # rows = int(input("rows = ")) # past
    # for i in range(rows):
    #     print("*" * (i+1))

    for i in range(rows := int(input("rows = "))):  # present
        print("*" * (i + 1))

    test = None
    if mode := test:
        print(1)
