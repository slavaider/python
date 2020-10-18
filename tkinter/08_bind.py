from pprint import pprint
from tkinter import Tk, Button, Event


def leftclick(event):
    print('Вы нажали левую кнопку мыши')


def rightclick(event):
    print('Вы нажали правую кнопку мыши')


def print_event(event: Event):
    pprint(event.__dict__)


def callback1(event: Event): print('callback1')


def callback2(event: Event): print('callback2')


def callback3(event: Event): print('callback3')


def callback4(event: Event): print('callback4')


def callback_2(event: Event):
    print('Нажата кнопка', event.widget['text'])


def callback(event: Event):
    pprint(event.__dict__)


# Атрибуты Event
# serial - серийный номер события (все события)
# num - номер кнопки мыши (ButtonPress, ButtonRelease)
# focus - имеет ли окно фокус (Enter, Leave)
# height и width - ширина и высота окна (Configure, Expose)
# keycode - код нажатой клавиши (KeyPress, KeyRelease)
# state - состояние события
# (для ButtonPress, ButtonRelease, Enter, KeyPress, КeyRelease, Leave, Motion -
# в виде числа; для Visibility - в виде строки)
# time - время наступления события (все события)
# x и y - координаты мыши
# x_root и y_root - координаты мыши на экране (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
# char - набранный на клавиатуре символ (KeyPress, KeyRelease)
# send_event - см. документацию по X/Windows
# keysym - набранный на клавиатуре символ (KeyPress, KeyRelease)
# keysym_num - набранный на клавиатуре символ в виде числа (KeyPress, KeyRelease)
# type - тип события в виде числа (все события)
# widget - виджет, который получил событие (все события)
# delta - изменение при вращении колеса мыши (MouseWheel)

# Дополнительные методы
# bind_all - создаёт привязку для всех виджетов приложения.
# Отличие от привязки к окну верхнего уровня заключается в том,
# что в случае привязки к окну привязываются все виджеты этого окна,
# а этот метод привязывает все виджеты приложения (у приложения может быть несколько окон).

# bind_class - создаёт привязку для всех виджетов данного класса

# bindtags - позволяет изменить порядок обработки привязок.
# По умолчанию порядок следующий: виджет, класс, окно, all;
# где виджет - привязка к виджету (bind), класс - привязка к классу (bind_class),
# окно - привязка к окну (root.bind), all - привязка всех виджетов (bind_all).

# unbind - отвязать виджет от события.
# В качестве аргумента принимает идентификатор, полученный от метода bind.

# unbind_all - то же, что и unbind, только для метода bind_all.
# unbind_class - то же, что и unbind, только для метода bind_class.
if __name__ == '__main__':
    root = Tk()
    btn = Button(root, text="1")
    btn.bind("<Button-1>", print_event)
    btn.pack()
    root.bind("z", callback)
    root.bind("<Control-Shift-KeyPress-q>", callback)
    root.bind("<<Button1>>", callback)

    button1 = Button(root, text='Нажми')
    button1.pack()
    button1.bind('<Button-1>', leftclick)
    button1.bind('<Button-3>', rightclick)

    button1 = Button(root, text='1')
    button2 = Button(root, text='2')
    root.bind_class('Button', '<1>', callback_2)
    button1.pack()
    button2.pack()

    root.mainloop()

# Список модификаторов
# Return - Enter
# Escape - Esc
# Control - Ctrl
# Alt
# Shift
# Lock
# Extended
# Prior - PgUp
# Next - PgDown
# Button1, B1 - нажата первая (левая) кнопка мыши
# Button2, B2 - вторая (средняя) кнопка мыши
# Button3, B3 - третья (правая)
# Button4, B4 - четвёртая
# Button5, B5 - пятая
# Mod1, M1, Command
# Mod2, M2, Option
# Mod3, M3
# Mod4, M4
# Mod5, M5
# Meta, M
# Double - двойной щелчок мыши (например, <Double-Button-1>)
# Triple - тройной
# Quadruple - четверной

# Типы событий
# Здесь перечислены все возможные типы событий, для самых часто используемых дано описание.
# Activate, Deactivate
# MouseWheel - прокрутка колесом мыши
# KeyPress, KeyRelease - нажатие и отпускание клавиши на клавиатуре
# ButtonPress, ButtonRelease, Motion - нажатие, отпускание клавиши мыши, движение мышью
# Configure - изменение положения или размера окна
# Map, Unmap - показывание или сокрытие окна (например, в случае сворачивания/разворачивания окна пользователем)
# Visibility
# Expose - событие генерируется, когда необходимо всё окно или его часть перерисовать
# Destroy - закрытие окна
# FocusIn, FocusOut - получение или лишение фокуса
# Enter, Leave - Enter генерируется когда курсор мыши "входит" в окно, Leave - когда "уходит" из окна
# Property
# Colormap
# MapRequest, CirculateRequest, ResizeRequest, ConfigureRequest, Create
# Gravity, Reparent, Circulate
