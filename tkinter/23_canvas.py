from tkinter import Tk, Canvas

if __name__ == '__main__':
    root = Tk()
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    # create canvas
    canvas = Canvas(root, width=500, height=500, bg="lightblue", cursor="arrow")
    # create lines
    canvas.create_line(200, 50, 300, 50, width=3, fill="blue")
    canvas.create_line(0, 0, 100, 100, width=2, arrow='last')
    # create rectangles
    x = 75
    y = 110
    canvas.create_rectangle(x, y, x + 80, y + 50, fill="white", outline="blue")
    # create polygon
    canvas.create_polygon([250, 100], [200, 150], [300, 150], fill="yellow")
    canvas.create_polygon([300, 80], [400, 80], [450, 75], [450, 200],
                          [300, 180], [330, 160], outline="white", smooth=1)
    # create oval
    canvas.create_oval([20, 200], [150, 300], fill="gray50")
    # create arc
    canvas.create_arc([160, 230], [230, 330], start=0, extent=140, fill="lightgreen")
    canvas.create_arc([250, 230], [320, 330], start=0, extent=140, style='chord', fill="green")
    canvas.create_arc([340, 230], [410, 330], start=0, extent=140, style='arc', outline="darkgreen", width=2)
    # create text
    canvas.create_text(20, 330,
                       text="Опыты с графическими примитивами\nна холсте",
                       font="Verdana 12",
                       anchor="w",
                       justify='center',
                       fill="red")

    x = 10
    while x < 450:
        canvas.create_rectangle(x, 400, x + 50, 450)
        x = x + 60
    canvas.pack()
    root.mainloop()
