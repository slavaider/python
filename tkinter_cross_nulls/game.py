from PIL import ImageTk
import random
from tkinter import Tk, Canvas, Label
import tkinter.messagebox as messagebox


def player_paint(event, current_sign, board):
    if current_sign:
        tk_image = ImageTk.PhotoImage(file='../files/cross.png')
    else:
        tk_image = ImageTk.PhotoImage(file='../files/null.png')

    label = Label(root, width=50, height=50, image=tk_image, bg=color)
    label.image = tk_image

    if (0 < event.x < 100) and (0 < event.y < 100):
        label.place(x=25, y=25)
        board[0] = 1
    elif (0 < event.x < 100) and (100 < event.y < 200):
        label.place(x=25, y=125)
        board[1] = 1
    elif (0 < event.x < 100) and (200 < event.y < 300):
        label.place(x=25, y=225)
        board[2] = 1
    elif (100 < event.x < 200) and (0 < event.y < 100):
        label.place(x=125, y=25)
        board[3] = 1
    elif (100 < event.x < 200) and (100 < event.y < 200):
        label.place(x=125, y=125)
        board[4] = 1
    elif (100 < event.x < 200) and (200 < event.y < 300):
        label.place(x=125, y=225)
        board[5] = 1
    elif (200 < event.x < 300) and (0 < event.y < 100):
        label.place(x=225, y=25)
        board[6] = 1
    elif (200 < event.x < 300) and (100 < event.y < 200):
        label.place(x=225, y=125)
        board[7] = 1
    elif (200 < event.x < 300) and (200 < event.y < 300):
        label.place(x=225, y=225)
        board[8] = 1


def machine_paint(index, current_sign):
    if current_sign:
        tk_image = ImageTk.PhotoImage(file='../files/cross.png')
    else:
        tk_image = ImageTk.PhotoImage(file='../files/null.png')

    label = Label(root, width=50, height=50, image=tk_image, bg=color)
    label.image = tk_image

    if index == 0:
        label.place(x=25, y=25)
    elif index == 1:
        label.place(x=25, y=125)
    elif index == 2:
        label.place(x=25, y=225)
    elif index == 3:
        label.place(x=125, y=25)
    elif index == 4:
        label.place(x=125, y=125)
    elif index == 5:
        label.place(x=125, y=225)
    elif index == 6:
        label.place(x=225, y=25)
    elif index == 7:
        label.place(x=225, y=125)
    elif index == 8:
        label.place(x=225, y=225)


def get_winner(state, combination):
    for x, y, z in combination:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 1 or state[x] == 2):
            return state[x]
    if 0 not in state:
        return "-"
    return ''


def cross_null_versus_computer(event):
    global flag
    player_paint(event, flag, board)
    flag = not flag
    while True:
        if 0 not in board:
            break
        index = random.randint(0, 8)
        if board[index] != 1 and board[index] != 2:
            machine_paint(index, flag)
            board[index] = 2
            flag = not flag
            break
    winner_sign = get_winner(board, winning_combination)

    if winner_sign != '' and winner_sign == 1:
        messagebox.showinfo("Game end", "Победитель:X")
        root.destroy()
    elif winner_sign != '' and winner_sign == 2:
        messagebox.showinfo("Game end", "Победитель:0")
        root.destroy()
    elif winner_sign == "-":
        messagebox.showinfo("Game end", "Ничья")
        root.destroy()


if __name__ == '__main__':
    # Constants
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    winning_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                           (2, 5, 8), (2, 4, 6), (0, 4, 8)]
    flag = True
    color = 'lightblue'

    root = Tk()
    root.title('Cross and nulls')
    size_width = 300
    size_height = 300
    root.minsize(width=size_width, height=size_height)
    root.maxsize(width=size_width, height=size_height)
    # create canvas
    canvas = Canvas(root, width=size_width, height=size_height, cursor="arrow")
    canvas.pack()
    # rectangles
    j = 0
    for i in range(0, size_width, 100):
        canvas.create_rectangle(i, 0, i + 100, 100, tag=f'tag{j}', fill=color)
        canvas.create_rectangle(i, 100, i + 100, 200, tag=f'tag{j + 1}', fill=color)
        canvas.create_rectangle(i, 200, i + 100, 300, tag=f'tag{j + 2}', fill=color)
        j += 3
    # Events
    canvas.tag_bind('tag0', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag1', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag2', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag3', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag4', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag5', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag6', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag7', '<Button-1>', cross_null_versus_computer)
    canvas.tag_bind('tag8', '<Button-1>', cross_null_versus_computer)

    root.mainloop()
