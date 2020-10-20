from tkinter import Tk, Canvas


def oval_func(event):
    canvas.delete(oval)
    canvas.create_text(30, 10, text="Здесь был круг", anchor="w")


def rect_func(event):
    canvas.delete("rect")
    canvas.create_text(180, 10, text="Здесь был\nпрямоугольник", anchor="nw")


def triangle_func(event):
    canvas.create_polygon(350, 70, 380, 20, 410, 70, fill='yellow', outline="black")


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(width=460, height=100, bg='grey80')
    canvas.pack()

    oval = canvas.create_oval(30, 10, 130, 80, fill="orange")
    canvas.create_rectangle(180, 10, 280, 80, tag="rect", fill="lightgreen")
    triangle = canvas.create_polygon(330, 80, 380, 10, 430, 80, fill='white', outline="black")

    canvas.tag_bind(oval, '<Button-1>', oval_func)
    canvas.tag_bind("rect", '<Button-1>', rect_func)
    canvas.tag_bind(triangle, '<Button-1>', triangle_func)

    root.mainloop()
