from tkinter import Tk, Entry, Button, Text


def output(event):
    s = entry.get()
    if s == "1":
        text.delete(1.0, 'end')
        text.insert('end', "Обслуживание клиентов на втором этаже")
    elif s == "2":
        text.delete(1.0, 'end')
        text.insert('end', "Пластиковые карты выдают в соседнем здании")
    else:
        text.delete(1.0, 'end')
        text.insert('end', "Введите 1 или 2 в поле слева")


if __name__ == '__main__':
    root = Tk()
    entry = Entry(root, width=1)
    button = Button(root, text="Вывести")
    text = Text(root, width=20, height=3, font="12", wrap='word')
    button.bind("<Button-1>", output)
    # Grid
    entry.grid(row=0, column=0, padx=20)
    button.grid(row=0, column=1)
    text.grid(row=0, column=2, padx=20, pady=10)
    root.mainloop()
