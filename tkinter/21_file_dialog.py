from tkinter import Tk, Text, Menu
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

import fileinput


def close_win():
    if messagebox.askyesno("Exit", "Do you want to save?"):
        save_file()
        root.destroy()
    else:
        root.destroy()


def about():
    messagebox.showinfo("Editor", "This is text editor.\n(test version)")


def open_file():
    txt.delete('1.0', 'end')
    open_file_path = filedialog.askopenfilename()
    for i in fileinput.input(open_file_path):
        txt.insert('end', i)


def save_file():
    save_file_path = filedialog.asksaveasfilename()
    if save_file_path:
        letter = txt.get(1.0, 'end')
        with open(save_file_path, "w") as file:
            file.write(letter)


if __name__ == '__main__':
    root = Tk()
    txt = Text(root, width=40, height=15, font="12")
    txt.pack()
    # add root_menu
    root_menu = Menu(root)
    root.config(menu=root_menu)
    # add side_menu
    side_menu = Menu(root_menu)
    root_menu.add_cascade(label='File', menu=side_menu)
    # add commands to side_menu
    side_menu.add_command(label="Open", command=open_file)
    side_menu.add_command(label="Save", command=save_file)
    side_menu.add_command(label="Exit", command=close_win)
    # add second_side_menu and command
    second_side_menu = Menu(root_menu)
    root_menu.add_cascade(label="Help", menu=second_side_menu)
    second_side_menu.add_command(label="About", command=about)

    root.mainloop()
