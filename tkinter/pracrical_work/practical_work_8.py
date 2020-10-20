import time
from tkinter import Tk, Canvas


def motion():
    canvas.move(rect, 1, 0)
    if canvas.coords(rect)[2] < 450:
        root.after(20, motion)


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(width=460, height=100, bg='grey80')
    canvas.pack()
    rect = canvas.create_rectangle(10, 10, 100, 80, tag="rect", fill="lightgreen")
    motion()
    root.mainloop()
