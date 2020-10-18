from tkinter import Tk, Frame, Button

colors = ["red", "green"]


def color(event):
    frame.configure(bg=colors[0])
    colors[0], colors[1] = colors[1], colors[0]


def out_go(event):
    root.destroy()


if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, width=100, height=100)
    button = Button(root, text="Выход")
    frame.pack()
    button.pack()
    root.bind("<Return>", color)
    button.bind("<Button-1>", out_go)
    root.mainloop()
