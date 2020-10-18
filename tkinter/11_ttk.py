from tkinter import Tk, ttk

#  ttk: Button,
#  Checkbutton,
#  Entry,
#  Frame,
#  Label,
#  LabelFrame,
#  Menubutton,
#  PanedWindow,
#  Radiobutton,
#  Scale и Scrollbar.
#  Кроме того имеется несколько новых виджетов:
#  Combobox,
#  Notebook,
#  Progressbar,
#  Separator,
#  Sizegrip и Treeview.
if __name__ == '__main__':
    root = Tk()
    button = ttk.Button(root, text="button")
    check_button = ttk.Checkbutton(root, text="check_button")
    entry = ttk.Entry(root)
    frame = ttk.Frame(root)
    Label = ttk.Label(root, text="test")
    labelFrame = ttk.Labelframe(root)
    Menubutton = ttk.Menubutton(root, text="4")
    PanedWindow = ttk.Panedwindow(root)
    Radiobutton = ttk.Radiobutton(root, text='5')
    Scale = ttk.Scale(root)
    Scrollbar = ttk.Scrollbar(root)
    Notebook = ttk.Notebook(root)
    Separator = ttk.Separator(root)
    Sizegrip = ttk.Sizegrip(root)
    Treeview = ttk.Treeview(root)
    # Pack
    button.pack()
    check_button.pack()
    entry.pack()
    frame.pack()
    Label.pack()
    labelFrame.pack()
    Menubutton.pack()
    PanedWindow.pack()
    Radiobutton.pack()
    Scale.pack()
    Scrollbar.pack()
    Notebook.pack()
    Separator.pack()
    Sizegrip.pack()
    Treeview.pack()
    root.mainloop()
