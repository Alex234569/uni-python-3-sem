# Программа запускает окно, в котором нарисована окружность
# Нажатие кнопки 'Start' запускает движение точки по окружности
# Вверху окна можно выбрать скорость и направление движения точки


import tkinter
from time import sleep
from math import sin
from math import cos
from math import pi


# Нажатие кнопки запускает движение точки по окружности
# Точка совершает один оборот по окружности
def start_button_click():
    speed = int(speed_options.get())
    if direction_options.get() == 'Clockwise':
        direction = 1
    else:
        direction = -1
    
    for i in range(0, 100 * direction, direction):
        canvas.create_oval(size//2 + r*cos(2*pi*i/100) - 3, 
                           size//2 + r*sin(2*pi*i/100) - 3, 
                           size//2 + r*cos(2*pi*i/100) + 3,
                           size//2 + r*sin(2*pi*i/100) + 3,
                           tags='dot', fill='green')
        root.update()
        sleep(0.05 / speed) # Ожидание для создания эффекта анимации
        canvas.delete('dot')
        root.update()


root = tkinter.Tk()
root.title('Traveling dot')

# Выпадающее меню выбора скорости точки
lbl1 = tkinter.Label(root, text='Choose dot speed:')
lbl1.pack(anchor='nw')
speed_options = tkinter.StringVar(root)
speed_options.set('1')
spd_opt_menu = tkinter.OptionMenu(root, speed_options, '1', '2', '3')
spd_opt_menu.pack(anchor='nw')

# Выпадющее меню выбора направления движения точки
lbl2 = tkinter.Label(root, text='Choose direction of roration:')
lbl2.pack(anchor='nw')
direction_options = tkinter.StringVar(root)
direction_options.set('Clockwise')
drct_opt_menu = tkinter.OptionMenu(root, direction_options, 'Clockwise',
                                   'Counterclockwise')
drct_opt_menu.pack(anchor='nw')

# Кнопка запуска анимации
start_button = tkinter.Button(text='Start', command=start_button_click)
start_button.pack()

# Поле для рисования
size = 600
canvas = tkinter.Canvas(root, width=size, height=size)
canvas.pack()

# Отрисовка окружности, по которой двигается точка
r = 200
canvas.create_oval(size//2 - r, size//2 - r, size//2 + r, size//2 + r)
root.update()
root.mainloop()
