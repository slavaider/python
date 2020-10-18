from tkinter import Tk, PhotoImage, Button

if __name__ == '__main__':
    # PhotoImage
    # file - путь к файлу с изображением.
    # data - вместо пути к файлу можно указать уже загруженные в память данные изображения.
    # Изображения в формате GIF могут быть закодированы с использованием base64.
    # Данная возможность удобна для встраивания изображения в программу.

    # format - явное указание формата изображения.
    # width, height - ширина и высота изображения.
    # gamma - коррекция гаммы.
    # palette - палитра изображения.
    root = Tk()
    image = PhotoImage(file='../files/cross.png', format='png')
    button = Button(root, image=image)
    button.pack()
    root.mainloop()
