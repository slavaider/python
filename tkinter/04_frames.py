from tkinter import Frame, Button, Tk, IntVar, Checkbutton, Radiobutton, Scale, Text, Scrollbar, Listbox


def get_value():
    a = scale1.get()
    print("Значение", a)


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
    check_button1 = Checkbutton(root, text='1 пункт', variable=var1, onvalue=1, offvalue=0)
    check_button2 = Checkbutton(root, text='2 пункт', variable=var2, onvalue=1, offvalue=0)
    check_button1.pack()
    check_button2.pack()
    # Radiobutton
    var = IntVar()
    var.set(1)
    radio_button1 = Radiobutton(root, text='1', variable=var, value=1)
    radio_button2 = Radiobutton(root, text='2', variable=var, value=2)
    radio_button3 = Radiobutton(root, text='3', variable=var, value=3)
    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()
    # Scale
    # orient - как расположена шкала на окне. Возможные значения: horizontal, vertical (горизонтально, вертикально).
    # length - длина шкалы.
    # from_ - с какого значения начинается шкала.
    # to - каким значением заканчивается шкала.
    # tickinterval - интервал, через который отображаются метки шкалы.
    # resolution - шаг передвижения (минимальная длина, на которую можно передвинуть движок)
    scale1 = Scale(root, orient='horizontal', length=300, from_=50, to=80, tickinterval=5,
                   resolution=5)
    button1 = Button(root, text="Получить значение", command=get_value)
    scale1.pack()
    button1.pack()
    # scrollbar
    text = Text(root, height=3, width=60)
    text.pack(side='left')
    scrollbar = Scrollbar(root)
    scrollbar.pack(side='left')
    # первая привязка
    scrollbar['command'] = text.yview
    # вторая привязка
    text['yscrollcommand'] = scrollbar.set
    # ListBox
    r = ['Linux', 'Python', 'Tk', 'Tkinter']
    lis = Listbox(root, selectmode='single', height=4)
    for i in r:
        lis.insert('end', i)
    lis.pack()
    root.mainloop()
