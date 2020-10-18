from tkinter import Tk, Frame, Button, Label, Text


def button1_event(event):
    frame['width'] = 100
    frame['height'] = 100


def button2_event(event):
    frame['width'] = 200
    frame['height'] = 200


def button3_event(event):
    frame['width'] = 300
    frame['height'] = 300


def wrap_text(event):
    label['text'] = text.get('1.0', 'end')


if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, width=100, height=100, bg='lime')
    button1 = Button(root, text="1")
    button2 = Button(root, text="2")
    button3 = Button(root, text="3")

    button1.bind("<Button-1>", button1_event)
    button2.bind("<Button-1>", button2_event)
    button3.bind("<Button-1>", button3_event)

    frame.pack()
    button1.pack()
    button2.pack()
    button3.pack()

    label = Label(root, text="Метка")
    text = Text(root, width=30, height=5, wrap='word')
    text.bind('<Return>', wrap_text)
    label.pack()
    text.pack()
    root.mainloop()
