from tkinter import Tk, Label


def b1(event):
    label['text'] = "Левая кнопка мыши"


def b3(event):
    label['text'] = "Правая кнопка мыши"


def move(event):
    label['text'] = "Движение мышью"


if __name__ == '__main__':
    root = Tk()
    root.minsize(width=500, height=400)
    label = Label(root, text='Test')
    label.pack()
    root.bind('<Button-1>', b1)
    root.bind('<Button-3>', b3)
    root.bind('<Motion>', move)

    root.mainloop()
