from tkinter import Tk, BitmapImage, Button

if __name__ == '__main__':
    # BitmapImage
    # Конструктор класса принимает следующие аргументы:
    # background и foreground - цвета фона и переднего плана для изображения.
    # Поскольку изображение двухцветное, то эти параметры определяют соответственно чёрный и белый цвет.

    # file и maskfile - пути к файлу с изображением и к маске
    # (изображению, указывающему какие пиксели будут прозрачными).

    # data и maskdata - вместо пути к файлу можно указать уже загруженные в память данные изображения.
    # Данная возможность удобна для встраивания изображения в программу.
    root = Tk()
    data = '''
    #define image_width 15
    #define image_height 15
    static unsigned char image_bits[] = {
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x1c, 0x30, 0x0c, 0x60, 0x06,
       0x60, 0x06, 0xc0, 0x03, 0xc0, 0x03, 0x60, 0x06, 0x60, 0x06, 0x30, 0x0c,
       0x38, 0x1c, 0x00, 0x00, 0x00, 0x00 };'''
    image = BitmapImage(data=data, background='red', foreground='black')
    button = Button(root, image=image)
    button.pack()
    root.mainloop()
