from tkinter import Tk, Canvas


def move(event):
    canvas.move(rectangle, 0, 2)


def color(event):
    canvas.itemconfig('group1', fill="red", width=3)


def clean(event):
    canvas.delete('all')


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(width=460, height=460, bg='grey80')
    canvas.pack()
    oval = canvas.create_oval(30, 10, 130, 80)
    rectangle = canvas.create_rectangle(180, 10, 280, 80)
    triangle = canvas.create_polygon(330, 80, 380, 10, 430, 80, fill='grey80', outline="black")
    # move
    canvas.move(rectangle, 0, 150)
    canvas.itemconfig(triangle, outline="red", width=3)
    canvas.coords(oval, 300, 200, 450, 450)
    # tag
    oval = canvas.create_oval(30, 10, 130, 80, tag="group1")
    canvas.create_line(10, 100, 450, 100, tag="group1")

    canvas.bind('<Button-1>', move)
    canvas.bind('<Return>', clean)
    canvas.bind('<Button-3>', color)
    root.mainloop()
