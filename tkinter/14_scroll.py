from tkinter import Tk, Text, Scrollbar, Toplevel

if __name__ == '__main__':
    root = Tk()
    tx = Text(root, width=30, height=3, font='14')
    scr = Scrollbar(root, command=tx.yview)
    tx.configure(yscrollcommand=scr.set)
    tx.grid(row=0, column=0)
    scr.grid(row=0, column=1)

    win = Toplevel(root, relief='sunken', bd=10, bg="lightblue")
    win.title("Дочернее окно")
    win.minsize(width=400, height=200)
    root.mainloop()
