from tkinter import Frame, Button, Tk, IntVar, Checkbutton, Radiobutton
# time break
if __name__ == '__main__':
    root = Tk()
    # Frame
    frame1 = Frame(root, bg='green', bd=2)
    frame2 = Frame(root, bg='red', bd=2)
    button1 = Button(frame1, text='Первая кнопка')
    button2 = Button(frame2, text='Вторая кнопка')
    frame1.pack()
    frame2.pack()
    button1.pack()
    button2.pack()
    # Checkbutton
    var1 = IntVar()
    var2 = IntVar()
    check1 = Checkbutton(root, text=u'1 пункт', variable=var1, onvalue=1, offvalue=0)
    check2 = Checkbutton(root, text=u'2 пункт', variable=var2, onvalue=1, offvalue=0)
    check1.pack()
    check2.pack()
    # Radiobutton
    var = IntVar()
    rbutton1 = Radiobutton(root, text='1', variable=var, value=1)
    rbutton2 = Radiobutton(root, text='2', variable=var, value=2)
    rbutton3 = Radiobutton(root, text='3', variable=var, value=3)
    rbutton1.pack()
    rbutton2.pack()
    rbutton3.pack()

    root.mainloop()
