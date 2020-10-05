def print_pool(f_sticks):
    print(f'Текущее число палочек {f_sticks}')


def check_pool(f_sticks):
    return 0 < f_sticks <= sticks


def check_sticks_between_1_and_3(choice):
    return 1 <= choice <= 3


sticks = 10
flag = True  # first player
print_pool(sticks)
while sticks > 0:
    if flag:
        player1_choice = int(input("Игрок 1 введите число палочек = "))
        if check_sticks_between_1_and_3(player1_choice):
            sticks -= player1_choice
            if check_pool(sticks):
                print_pool(sticks)
                flag = not flag
            else:
                print("Игрок 2 выйграл")
        else:
            print("Выбор палочек должны быть в предела от 1 до 3")
            continue
    else:
        player2_choice = int(input("Игрок 2 введите число палочек = "))
        if check_sticks_between_1_and_3(player2_choice):
            sticks -= player2_choice
            if check_pool(sticks):
                print_pool(sticks)
                flag = not flag
            else:
                print("Игрок 1 выйграл")
        else:
            print("Выбор палочек должны быть в предела от 1 до 3")
            continue
