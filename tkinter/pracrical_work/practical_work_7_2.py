from tkinter import Tk, Canvas

if __name__ == '__main__':
    root = Tk()
    size_width = 400
    size_height = 500
    root.minsize(width=size_width, height=size_height)
    root.maxsize(width=size_width, height=size_height)
    # create canvas
    canvas = Canvas(root, width=size_width, height=size_height, cursor="arrow")
    # rectangles
    for i in range(11):
        canvas.create_rectangle(180, 33 * (i + 1), 230, 33 * (i + 2), fill='yellow')
    canvas.create_rectangle(50, 33, 100, 150, fill='light green')
    canvas.create_rectangle(300, 33, 350, 200, fill='light blue')
    # Lines
    # Left
    canvas.create_line(180, 310, 15, 310, width=2)
    canvas.create_line(15, 310, 15, 60, width=2)
    canvas.create_line(15, 60, 50, 60, width=2, arrow='last')
    # Centre
    canvas.create_line(180, 80, 130, 80, width=2)
    canvas.create_line(130, 80, 130, 60, width=2)
    canvas.create_line(130, 60, 100, 60, width=2, arrow='last')
    # Right
    canvas.create_line(230, 150, 270, 150, width=2)
    canvas.create_line(270, 150, 270, 60, width=2)
    canvas.create_line(270, 60, 300, 60, width=2, arrow='last')
    # Text
    canvas.create_text(75, 20, text='F1', font='20')
    canvas.create_text(205, 20, text='P', font='20')
    canvas.create_text(325, 20, text='F2', font='20')
    canvas.create_text(320, 450, text='P - main program\nF1 - function 1\nF2 - function 2', font='20')
    canvas.pack()
    root.mainloop()
