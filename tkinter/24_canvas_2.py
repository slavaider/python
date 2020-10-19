from tkinter import Tk, Canvas


def move(event):
    canvas.move(rectangle, 0, 2)


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

    canvas.bind('<Button-1>', move)
    root.mainloop()
