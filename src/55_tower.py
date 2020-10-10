def solve_tower(disks):
    return 2 ** disks - 1


if __name__ == '__main__':
    print(solve_tower(int(input("Введите высоту башни = "))))
