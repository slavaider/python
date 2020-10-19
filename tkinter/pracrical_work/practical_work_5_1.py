from tkinter import Tk, Text, IntVar, Checkbutton, Label


def on(event):
    label['text'] = ''
    result = ''
    for i in all_values:
        if i.get() == 1:
            result += f'button {all_buttons[all_values.index(i)]},'
    if result != '' and result[-1] == ',':
        result = result[0:-1]
    label['text'] = 'ON: ' + result


def off(event):
    label['text'] = ''
    result = ''
    for i in all_values:
        if i.get() == 0:
            result += f'button {all_buttons[all_values.index(i)]},'
    if result != '' and result[-1] == ',':
        result = result[0:-1]
    label['text'] = 'OFF: ' + result


if __name__ == '__main__':
    root = Tk()
    value1 = IntVar()
    value2 = IntVar()
    value3 = IntVar()
    all_values = [value1, value2, value3]
    check_button1 = Checkbutton(root, text='1', variable=value1, offvalue=0, onvalue=1)
    check_button2 = Checkbutton(root, text='2', variable=value2, offvalue=0, onvalue=1)
    check_button3 = Checkbutton(root, text='3', variable=value3, offvalue=0, onvalue=1)
    all_buttons = [check_button1['text'], check_button2['text'], check_button3['text']]
    check_button1.pack()
    check_button2.pack()
    check_button3.pack()
    label = Label(root)
    label.pack()
    root.bind('<Button-1>', on)
    root.bind('<Button-3>', off)
    root.mainloop()
