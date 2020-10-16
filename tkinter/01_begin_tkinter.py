import math
import time
from random import random
from tkinter import Tk, ttk, Button, Label, Entry, Text, Listbox


def window_deleted():
    print('Окно закрыто')
    root.quit()  # явное указание на выход из программы


def hello():
    print("Hello World!")


def btn3():
    btn3['text'] = time.strftime('%H:%M:%S')


def btn4():
    btn4['text'] = f'previous {btn4["bg"]}'  # показываем предыдущий цвет кнопки
    btn4['bg'] = '#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16))


def btn5():
    if label.winfo_viewable():
        label.grid_remove()
    else:
        label.grid()


def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')


def hard_job():
    pass
    # x = 1000
    # while True:
    #     x = math.log(x) ** 2.8
    #     root.update()


def btn7():
    text.delete('1.0', 'end')  # Удалить все


def btn8():
    response = text.get('1.0', 'end')  # Извлечь все
    print(response)


if __name__ == '__main__':
    root = Tk()
    # Configuration
    root.title(u'Пример приложения')
    root.geometry('500x400+300+200')  # ширина=500, высота=400, x=300, y=200
    root.protocol('WM_DELETE_WINDOW', window_deleted)  # обработчик закрытия окна
    root.resizable(True, False)  # размер окна может быть изменён только по горизонтали
    # btn1
    btn1 = Button(root,  # родительское окно
                  text="Click me",  # надпись на кнопке
                  bg="green", fg="black",  # цвет фона и надписи
                  command=hello)  # функция
    # btn2
    btn2 = ttk.Button(root, text="Hello World", command=hello)
    # btn3
    btn3 = Button(root)
    btn3.configure(text=time.strftime('%H:%M:%S'), command=btn3)
    # btn4
    btn4 = Button(root, command=btn4, text='random color', bg='white')
    # btn5
    btn5 = Button(root, command=btn5, text='Спрятать/показать')
    # label
    label = Label(font='sans 20')
    label.after_idle(tick)
    # btn6
    btn6 = Button(root, text='ok', width=10, height=1, bg='black', fg='red', font='arial 14')
    # entry_page
    entry = Entry(root,
                  borderwidth='1',  # ширина бордюра элемента
                  bd='1',  # сокращение от borderwidth
                  width='15',  # задаёт длину элемента в  знакоместах.
                  show='@', )  # задает  отображаемый символ.
    # Text

    text = Text(root, height=5, width=15, font='Arial 10', wrap='word')
    text.insert(1.0, 'Добавить Текст\nв начало первой строки')
    btn7 = Button(root, text='Удалить все', command=btn7)
    btn8 = Button(root, text=' Извлечь все', command=btn8)
    # List boxes
    listbox1 = Listbox(root, height=5, width=15, selectmode='extended')
    listbox2 = Listbox(root, height=5, width=15, selectmode='single')
    list1 = ["Москва", "Санкт-Петербург", "Саратов", "Омск"]
    list2 = ["Канберра", "Сидней", "Мельбурн", "Аделаида"]
    for i in list1:
        listbox1.insert('end', i)
    for i in list2:
        listbox2.insert('end', i)
    # Positional
    # column 0
    label.grid(row=0, column=0)
    btn1.grid(row=1, column=0)
    btn2.grid(row=2, column=0)
    btn3.grid(row=3, column=0)
    btn4.grid(row=4, column=0)
    btn5.grid(row=5, column=0)
    btn6.grid(row=6, column=0)
    # column 1
    entry.grid(row=0, column=1)
    text.grid(row=1, column=1)
    btn7.grid(row=2, column=1)
    btn8.grid(row=3, column=1)
    listbox1.grid(row=4, column=1)
    listbox2.grid(row=5, column=1)

    root.after(500, hard_job)
    root.mainloop()
