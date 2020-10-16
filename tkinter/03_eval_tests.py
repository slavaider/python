from tkinter import Tk

if __name__ == '__main__':
    root = Tk()
    root.eval('package require tile; ttk::style theme use clam')
    root.eval('ttk::button .b -text {ttk button}; pack .b')
    root.mainloop()
