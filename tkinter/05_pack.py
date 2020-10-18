from tkinter import Button, Tk

if __name__ == '__main__':
    # Pack
    # Аргументы
    # side ("left"/"right"/"top"/"bottom") - к какой стороне должен примыкать размещаемый виджет.
    # fill (None/"x"/"y"/"both") - необходимо ли расширять пространство предоставляемое виджету.
    # expand (True/False) - необходимо ли расширять сам виджет, чтобы он занял всё предоставляемое ему пространство.
    # in_ - явное указание в какой родительский виджет должен быть помещён.

    # Дополнительные функции:
    # pack_configure - синоним для pack.
    # pack_slaves (синоним slaves) - возвращает список всех дочерних упакованных виджетов.
    # pack_info - возвращает информацию о конфигурации упаковки.

    # pack_propagate
    # (синоним propagate) (True/False) - включает/отключает распространении информации о геометрии дочерних виджетов.
    # По умолчанию виджет изменяет свой размер в соответствии с размером своих потомков.
    # Этот метод может отключить такое поведение (pack_propagate(False)).
    # Это может быть полезно, если необходимо,
    # чтобы виджет имел фиксированный размер и не изменял его по прихоти потомков.

    # pack_forget (синоним forget) - удаляет виджет и всю информацию о его расположении из упаковщика.
    # Позднее этот виджет может быть снова размещён.

    root = Tk()
    button1 = Button(text="1")
    button2 = Button(text="2")
    button3 = Button(text="3")
    button4 = Button(text="4")
    button5 = Button(text="5")
    button1.pack(side='left')
    button2.pack(side='top')
    button3.pack(side='left')
    button4.pack(side='bottom')
    button5.pack(side='right')
    root.mainloop()
