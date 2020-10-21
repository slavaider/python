from tkinter import Tk, Canvas
from PIL import ImageTk


def stamp(event):
    canvas.create_image(event.x, event.y, image=tkimg)


if __name__ == '__main__':
    root = Tk()
    tkimg = ImageTk.PhotoImage(file='../files/null.png')
    canvas = Canvas(root, height=600, width=600, bg='green')
    canvas.grid()

    canvas.bind('<ButtonPress-1>', stamp)
    root.mainloop()
