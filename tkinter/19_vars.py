from tkinter import Tk, StringVar, Checkbutton, Listbox, Button, Entry


def result(event):
    v0 = var0.get()
    v1 = var1.get()
    v2 = var2.get()
    list_values = [v0, v1, v2]  # значения переменных заносятся в список
    list_box.delete(0, 2)  # предыдущее содержимое удаляется из Listbox
    for value in list_values:  # содержимое списка l последовательно ...
        list_box.insert('end', value)  # ...вставляется в Listbox


if __name__ == '__main__':
    root = Tk()
    var0 = StringVar()  # значение каждого флажка ...
    var1 = StringVar()  # ... хранится в собственной переменной
    var2 = StringVar()
    # если флажок установлен, то в ассоциированную переменную ...
    # ...(var0,var1 или var2) заносится значение onvalue, ...
    # ...если флажок снят, то - offvalue.
    check_button1 = Checkbutton(root, text="Окружность", variable=var0,
                                onvalue="circle", offvalue="-")
    check_button2 = Checkbutton(root, text="Квадрат", variable=var1,
                                onvalue="square", offvalue="-")
    check_button3 = Checkbutton(root, text="Треугольник", variable=var2,
                                onvalue="triangle", offvalue="-")
    list_box = Listbox(root, height=3)

    button = Button(root, text="Получить значения")
    button.bind('<Button-1>', result)

    check_button1.deselect()  # "по умолчанию" флажки сняты
    check_button2.deselect()
    check_button3.deselect()

    v = StringVar()
    ent1 = Entry(root, textvariable=v, bg="black", fg="white")
    ent2 = Entry(root, textvariable=v)

    ent1.pack()
    ent2.pack()
    check_button1.pack()
    check_button2.pack()
    check_button3.pack()
    button.pack()
    list_box.pack()

    root.mainloop()
