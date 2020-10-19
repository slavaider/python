from tkinter import Tk, Canvas

if __name__ == '__main__':
    root = Tk()
    size_width = 400
    size_height = 500
    root.minsize(width=size_width, height=size_height)
    root.maxsize(width=size_width, height=size_height)
    # create canvas
    canvas = Canvas(root, width=size_width, height=size_height, bg="lightblue", cursor="arrow")
    # rectangles
    for i in range(0, size_width, 100):
        canvas.create_rectangle(i, 0, i + 100, 100)
        canvas.create_rectangle(i, 200, i + 100, 100)
        canvas.create_rectangle(i, 300, i + 100, 100)
        canvas.create_rectangle(i, 400, i + 100, 100)
        canvas.create_rectangle(i, 500, i + 100, 100)
    # Text
    canvas.create_text(50, 50, text="X", font='12')
    canvas.create_text(150, 50, text="Y", font='12')
    canvas.create_text(250, 50, text="X and Y", font='12')
    canvas.create_text(350, 50, text="X or Y", font='12')
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    answer_and = []
    answer_or = []
    for i in range(len(x)):
        answer_and.append(int(x[i] and y[i]))
        answer_or.append(int(x[i] or y[i]))
    print(answer_or)
    for i in range(4):
        canvas.create_text(50, (100 * (i + 1)) + 50, text=x[i], font='12')
        canvas.create_text(150, (100 * (i + 1)) + 50, text=y[i], font='12')
        canvas.create_text(250, (100 * (i + 1)) + 50, text=answer_and[i], font='12')
        canvas.create_text(350, (100 * (i + 1)) + 50, text=answer_or[i], font='12')
    canvas.pack()
    root.mainloop()
