from tkinter import Tk, Frame, Canvas
from PIL import ImageTk, Image

if __name__ == '__main__':
    t = Tk()
    t.title("Transparency")

    frame = Frame(t)
    frame.pack()

    canvas = Canvas(frame, bg="black", width=500, height=500)
    canvas.pack()

    photoimage = ImageTk.PhotoImage(file="../files/cross.png")
    canvas.create_image(150, 150, image=photoimage)
    im = Image.open("../files/cross.png")
    print(im.mode)
    t.mainloop()
