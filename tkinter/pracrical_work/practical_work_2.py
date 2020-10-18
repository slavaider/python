from tkinter import Tk, Scale, Frame, Entry, Text, Scrollbar, Toplevel, Button

if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, bd=15, bg='lime')
    scale = Scale(frame, orient="horizontal", length=300, from_=0, to=100, tickinterval=10, resolution=10)
    frame.pack()
    scale.pack()

    frame2 = Frame(root, width=300, height=200, bg="green", bd=20)
    entry = Entry(frame2)
    frame2.pack()
    entry.pack()

    frame3 = Frame(root)
    text = Text(frame3, width=30, height=3)
    scroll = Scrollbar(frame3, command=text.yview)
    text.configure(yscrollcommand=scroll.set)
    text.grid(row=0, column=0)
    scroll.grid(row=0, column=1)
    frame3.pack()

    win1 = Toplevel(root, relief='sunken', bd=10, bg="lightblue")
    win1.title("Дочернее окно 1")
    win1.minsize(width=400, height=200)
    btn1 = Button(win1, text="1")
    btn1.pack()
    win2 = Toplevel(root, relief='sunken', bd=10, bg="blue")
    win2.title("Дочернее окно 2")
    win2.minsize(width=400, height=200)
    btn2 = Button(win2, text="2")
    btn2.pack()

    root.mainloop()
