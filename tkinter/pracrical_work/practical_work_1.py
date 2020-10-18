from tkinter import Tk, Entry, Text, Button, Radiobutton, Checkbutton, Frame, Label, Event, IntVar


def response():
    r1 = entry.get()
    r2 = text.get('1.0', 'end')
    print('Адрес: \n', r1)
    print('Коментарий: \n', r2)


if __name__ == '__main__':
    root = Tk()
    # Ex1
    frame1 = Frame(root)
    label1 = Label(frame1, text='Ваш адрес:')
    entry = Entry(frame1)
    label2 = Label(frame1, text='Коментарий:')
    text = Text(frame1, width='15', height='5')
    btn = Button(frame1, text='Отправить', bg='cyan', command=response)
    # Pack1
    frame1.pack()
    label1.pack()
    entry.pack()
    label2.pack()
    text.pack()
    btn.pack()
    # Ex2
    frame2 = Frame(root)
    label3 = Label(frame2, text='Сколько штук?')
    value = IntVar()
    value.set(1)
    rb1 = Radiobutton(frame2, text='0-10', variable=value, value=1)
    rb2 = Radiobutton(frame2, text='11-20', variable=value, value=2)
    rb3 = Radiobutton(frame2, text='21-30', variable=value, value=3)
    rb4 = Radiobutton(frame2, text='31-40', variable=value, value=4)
    label4 = Label(frame2, text='Какого цвета?')
    value_check_box1 = IntVar()
    value_check_box2 = IntVar()
    value_check_box3 = IntVar()
    value_check_box4 = IntVar()
    check_button1 = Checkbutton(frame2, text='RED', bg='red', variable=value_check_box1, onvalue=1, offvalue=0)
    check_button2 = Checkbutton(frame2, text='BLUE', bg='blue', variable=value_check_box2, onvalue=1, offvalue=0)
    check_button3 = Checkbutton(frame2, text='GREEN', bg='green', variable=value_check_box3, onvalue=1, offvalue=0)
    check_button4 = Checkbutton(frame2, text='YELLOW', bg='yellow', variable=value_check_box4, onvalue=1, offvalue=0)
    # Pack2
    frame2.pack()
    label3.pack()
    rb1.pack()
    rb2.pack()
    rb3.pack()
    rb4.pack()
    label4.pack()
    check_button1.pack()
    check_button2.pack()
    check_button3.pack()
    check_button4.pack()
    root.mainloop()
