from tkinter import Tk, Text, Button, Canvas, Entry


def erase():
    text.delete('3.0', '3.end')


def smiley(event):
    canvas = Canvas(height=30, width=30)
    canvas.create_oval(1, 1, 29, 29, fill="yellow")
    canvas.create_oval(9, 10, 12, 12)
    canvas.create_oval(19, 10, 22, 12)
    canvas.create_polygon(9, 20, 15, 24, 22, 20)
    text.window_create('current', window=canvas)


if __name__ == '__main__':
    root = Tk()
    # текстовое поле и его первоначальные настройки
    text = Text(font=('times', 12), width=50, height=15, wrap='word')
    text.pack(expand='yes', fill='both')
    text.insert(1.0, 'Дзэн Питона\n\
    Если интерпретатору Питона дать команду\n\
    import this ("импортировать это"),\n\
    то выведется так называемый "Дзен Питона".\n Некоторые выражения:\n\
    * Если реализацию сложно объяснить — это плохая идея.\n\
    * Ошибки никогда не должны замалчиваться.\n\
    * Явное лучше неявного.\n\n')
    # установка тегов для областей текста
    text.tag_add('title', '1.0', '1.end')
    text.tag_add('special', '6.0', '8.end')
    text.tag_add('special', '3.0', '3.11')
    text.tag_add('other', '3.11', '6.0')
    # конфигурирование тегов
    text.tag_config('title', foreground='red',
                    font=('times', 14, 'underline'), justify='center')
    text.tag_config('special', background='grey85', font=('Dejavu', 10, 'bold'))
    text.tag_config('other', background='red', font=('Verdana', 15, 'bold'))

    entry = Entry(text)
    button = Button(text, text='Стереть', command=erase)
    text.window_create('end', window=button)
    text.window_create('end', window=entry)
    text.bind('<Button-1>', smiley)
    root.mainloop()
