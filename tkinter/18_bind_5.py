from tkinter import Entry, Label, Tk


def exit_(event):
    root.destroy()


def caption(event):
    t = entry.get()
    label.configure(text=t)


if __name__ == '__main__':
    root = Tk()

    entry = Entry(root, width=40)
    label = Label(root, width=80)

    entry.pack()
    label.pack()

    entry.bind('<Return>', caption)
    root.bind('<Control-z>', exit_)

    root.mainloop()
