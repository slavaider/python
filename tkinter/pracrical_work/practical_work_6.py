from tkinter import Frame, Tk, Menu


def color_r():
    frame.config(bg="Red")


def color_g():
    frame.config(bg="Green")


def color_b():
    frame.config(bg="Blue")


def square():
    frame.config(width=500)
    frame.config(height=500)


def rectangle():
    frame.config(width=700)
    frame.config(height=400)


if __name__ == '__main__':
    root = Tk()

    frame = Frame(root, width=300, height=100, bg="Black")
    frame.pack()

    root_menu = Menu(root)
    root.config(menu=root_menu)

    menu1 = Menu(root_menu)
    root_menu.add_cascade(label="Color", menu=menu1)
    menu1.add_command(label="Red", command=color_r)
    menu1.add_command(label="Green", command=color_g)
    menu1.add_command(label="Blue", command=color_b)

    menu2 = Menu(root_menu)
    root_menu.add_cascade(label="Size", menu=menu2)
    menu2.add_command(label="500x500", command=square)
    menu2.add_command(label="700x400", command=rectangle)

    root.mainloop()
