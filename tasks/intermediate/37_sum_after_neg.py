if __name__ == '__main__':
    list_items = [5, 3, -1, 8, 0, -6, 1]
    res = 0
    for i in range(len(list_items)):
        if list_items[i] < 0:
            for j in range(list_items.index(list_items[i]) + 1, len(list_items)):
                res += abs(list_items[j])
            break
    print(list_items)
    print(res)
