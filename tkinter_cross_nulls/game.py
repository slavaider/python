from PIL import Image, ImageTk
import random
from tkinter import Tk, PhotoImage, Button, Canvas, Event, Label

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


def check_tag_of_event(event):
    if (0 < event.x < 100) and (0 < event.y < 100):
        return 'tag0'
    elif (0 < event.x < 100) and (100 < event.y < 200):
        return 'tag1'
    elif (0 < event.x < 100) and (200 < event.y < 300):
        return 'tag2'
    elif (100 < event.x < 200) and (0 < event.y < 100):
        return 'tag3'
    elif (100 < event.x < 200) and (100 < event.y < 200):
        return 'tag4'
    elif (100 < event.x < 200) and (200 < event.y < 300):
        return 'tag5'
    elif (200 < event.x < 300) and (0 < event.y < 100):
        return 'tag6'
    elif (200 < event.x < 300) and (100 < event.y < 200):
        return 'tag7'
    elif (200 < event.x < 300) and (200 < event.y < 300):
        return 'tag8'


def paint_cross_null(event):
    tag = check_tag_of_event(event)
    print(tag)
    path = Image.open('../files/null.png').convert("RGBA")
    path.fill
    image = ImageTk.PhotoImage(image=path)
    label = Label(image=image, width=76, height=76)
    label.image = image  # keep a reference!

    label.place(x=event.x - 50, y=event.y - 50)
    # canvas.itemconfigure(tag, fill='blue')


if __name__ == '__main__':

    # play_game(board)
    root = Tk()
    size_width = 300
    size_height = 300
    root.minsize(width=size_width, height=size_height)
    root.maxsize(width=size_width, height=size_height)
    # create canvas
    canvas = Canvas(root, width=size_width, height=size_height, cursor="arrow")
    # rectangles
    j = 0
    for i in range(0, size_width, 100):
        canvas.create_rectangle(i, 0, i + 100, 100, tag=f'tag{j}', fill='lightgreen')
        canvas.create_rectangle(i, 100, i + 100, 200, tag=f'tag{j + 1}', fill='lightgreen')
        canvas.create_rectangle(i, 200, i + 100, 300, tag=f'tag{j + 2}', fill='lightgreen')
        j += 3

    canvas.tag_bind('tag0', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag1', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag2', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag3', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag4', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag5', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag6', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag7', '<Button-1>', paint_cross_null)
    canvas.tag_bind('tag8', '<Button-1>', paint_cross_null)
    canvas.pack()
    root.mainloop()
