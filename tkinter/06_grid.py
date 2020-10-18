from tkinter import Tk, Entry, Button, Text, Scrollbar

if __name__ == '__main__':
    # Аргументы
    # row - номер строки, в который помещаем виджет.
    # rowspan - сколько строк занимает виджет
    # column - номер столбца, в который помещаем виджет.
    # columnspan - сколько столбцов занимает виджет.
    # padx / pady - размер внешней границы (бордюра) по горизонтали и вертикали.

    # ipadx / ipady - размер внутренней границы (бордюра) по горизонтали и вертикали.
    # Разница между pad и ipad в том, что при указании pad расширяется свободное пространство,
    # а при ipad расширяется помещаемый виджет.

    # sticky ("n", "s", "e", "w" или их комбинация) - указывает к какой границе "приклеивать" виджет.
    # Позволяет расширять виджет в указанном направлении.
    # Границы названы в соответствии со сторонами света.
    # "n" (север) - верхняя граница, "s" (юг) - нижняя, "w" (запад) - левая, "e" (восток) - правая.

    # in_ - явное указание в какой родительский виджет должен быть помещён.

    # Дополнительные функции
    # grid_configure - синоним для grid.
    # grid_slaves (синоним slaves) - см. pack_slaves.
    # grid_info - см. pack_info.
    # grid_propagate (синоним propagate) - см. pack_propagate.
    # grid_forget (синоним forget) - см. pack_forget.

    # grid_remove - удаляет виджет из-под управления упаковщиком, но сохраняет информацию об упаковке.
    # Этот метод удобно использовать для временного удаления виджета (см. пример в описании метода destroy).

    # grid_bbox (синоним bbox) - возвращает координаты (в пикселях) указанных столбцов и строк.
    # grid_location (синоним location) - принимает два аргумента: x и y (в пикселях).
    # Возвращает номер строки и столбца в которые попадают указанные координаты,
    # либо -1 если координаты попали вне виджета.

    # grid_size (синоним size) - возвращает размер таблицы в строках и столбцах.
    # grid_columnconfigure (синоним columnconfigure) и grid_rowconfigure (синоним rowconfigure)
    # - важные функции для конфигурирования упаковщика.
    # Методы принимают номер строки/столбца и аргументы конфигурации.

    # Список возможных аргументов:
    # minsize - минимальная ширина/высота строки/столбца.
    # weight - "вес" строки/столбца при увеличении размера виджета.
    # 0 означает, что строка/столбец не будет расширяться.
    # Строка/столбец с "весом" равным 2 будет расширяться вдвое быстрее, чем с весом 1.

    # uniform - объединение строк/столбцов в группы.
    # Строки/столбцы имеющие одинаковый параметр uniform будут расширяться строго в соответствии со своим весом.

    # pad - размер бордюра. Указывает, сколько пространства будет добавлено к самому большому виджету в строке/столбце.
    # 1 Пример
    root = Tk()
    entry1 = Entry(root)
    button1 = Button(text='1')
    button2 = Button(text='2')
    button3 = Button(text='3')
    entry1.grid(row=0, column=0, columnspan=3)
    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    # 2 Пример
    text = Text(wrap='none')
    vertical_scrollbar = Scrollbar(orient='vert', command=text.yview)
    text['yscrollcommand'] = vertical_scrollbar.set
    horizontal_scrollbar = Scrollbar(orient='hor', command=text.xview)
    text['xscrollcommand'] = horizontal_scrollbar.set
    # размещаем виджеты
    text.grid(row=0, column=0, sticky='nsew')
    vertical_scrollbar.grid(row=0, column=1, sticky='ns')
    horizontal_scrollbar.grid(row=1, column=0, sticky='ew')
    # конфигурируем упаковщик, чтобы текстовый виджет расширялся
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
