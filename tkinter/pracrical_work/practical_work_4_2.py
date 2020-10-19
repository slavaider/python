from tkinter import Tk, Frame, Entry


def change_size(event):
    int1 = int(entry1.get())
    int2 = int(entry2.get())
    frame.configure(width=int1, height=int2)


if __name__ == '__main__':
    root = Tk()
    root.minsize(width=500, height=400)
    entry1 = Entry(root)
    entry2 = Entry(root)
    frame = Frame(root, width=100, height=100, bg='cyan')
    entry1.pack()
    entry2.pack()
    frame.pack()
    root.bind('<space>', change_size)
    root.mainloop()
