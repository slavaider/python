from tkinter import Frame, Tk, Scale, IntVar


def change_color(variable, index, mode):
    frame['bg'] = '#%0x%0x%0x' % (var.get() * 16, var.get() * 16, var.get() * 16)


if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, width=100, height=100)
    var = IntVar()
    scale = Scale(root, orient='horizontal', variable=var, length=300, from_=0, to=99, tickinterval=10,
                  resolution=10)
    var.trace_add('write', change_color)
    frame.pack()
    scale.pack()
    root.mainloop()
