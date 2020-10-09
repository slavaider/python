if __name__ == '__main__':
    square = [[2, 3, 4], [6, 7, 7], [8, 9, 1]]
    temp = []
    for i in range(len(square)):
        temp += square[i]
    print(temp)
    for i in range(1, 9):
        if temp.count(i) > 1:
            print(f"{i} True")
            break
        else:
            continue
