import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winning_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                       (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def print_board(board_game):
    for i, cell in enumerate(board_game):
        if (i + 1) % 3 == 0:
            print(cell)
        else:
            print(cell + '|', end='')


def get_winner(state, combination):
    for x, y, z in combination:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == '0'):
            return state[x]
        elif state.count(' ') == 0:
            return "-"
    return ''


def play_game(board_game):
    current_sign = 'X'
    flag = True
    while get_winner(board_game, winning_combination) == '':
        if flag:
            index = int(input(f'Введите номер клетки от 0 - 8. Куда вы хотите поставить {current_sign} : '))
            flag = False
        else:
            while True:
                index = random.randint(0, 8)
                if board_game[index] == ' ':
                    break
            print(f"Компьютер выбирает ход = {index}")
            flag = True
        if board_game[index] == ' ':
            board_game[index] = current_sign
        else:
            flag = not flag
            continue
        print_board(board_game)
        winner_sign = get_winner(board_game, winning_combination)
        if winner_sign == "-":
            print("Ничья")
            break
        if winner_sign != '':
            print("Победитель " + winner_sign)
        current_sign = 'X' if current_sign == '0' else '0'


if __name__ == '__main__':
    play_game(board)
