from tkinter import Tk, Button

if __name__ == '__main__':
    # Place
    # Аргументы
    # anchor ("n", "s", "e", "w", "ne", "nw", "se", "sw" или "center") -
    # какой угол или сторона размещаемого виджета будет указана в аргументах x/y/relx/rely.
    # По умолчанию "nw" - левый верхний

    # bordermode ("inside", "outside", "ignore") -
    # определяет в какой степени будут учитываться границы при размещении виджета.

    # in_ - явное указание в какой родительский виджет должен быть помещён.
    # x и y - абсолютные координаты (в пикселях) размещения виджета.
    # width и height - абсолютные ширина и высота виджета.
    # relx и rely - относительные координаты (от 0.0 до 1.0) размещения виджета.
    # relwidth и relheight - относительные ширина и высота виджета.

    # Дополнительные функции
    # place_slaves, place_forget, place_info - см. описание аналогичных методов упаковщика pack.
    root = Tk()
    button1 = Button(text='1')
    button2 = Button(text='2')
    button1.place(relheight=1.0, height=-2)
    button2.place(relx=0.5, rely=0.5)
    root.mainloop()
