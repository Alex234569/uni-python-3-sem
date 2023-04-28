# Программа запускает окно, в котором точка, начиная с серидины экрана начинает
# двигаться по случайному пути. Внизу окна можно выбать приоритетное 
# направление движения и его "силу". Для удобства слежения за путём точки она
# оставляет за собой радужный след. Точка прекращает движенние, если выходит за
# границы поля для рисования


import tkinter
from random import randint
from time import sleep

# Окно
root = tkinter.Tk()
root.title('Random path')
root.configure(background='gray')

# Поле для рисования
size = 500
canvas = tkinter.Canvas(root, width=size, height=size, bg='gray', highlightthickness=0)
canvas.pack()

# Поле выбора приоритетного направления движения
# Значение "0" не меняет приоритетность движения
gravity = tkinter.Scale(root, from_=0, to=4, orient='horizontal')
gravity.pack()
gravity_directions_options = tkinter.StringVar(root)
gravity_directions_options.set('...')
grav_dir_menu = tkinter.OptionMenu(root, gravity_directions_options, '🡸', '🡼', '🡹', '🡽', '🡺', '🡾', '🡻', '🡿')
grav_dir_menu.pack()

# Начальное положение точки
x = size // 2
y = size // 2

# Переменные для задачи приоритетного направления движения
n = 0
s = 0
e = 0
w = 0

# Цвета, которые оставляет за собой точка
rainbow_colors = ['#FF0000', '#FF0F00', '#FF1F00', '#FF2F00',
                  '#FF3F00', '#FF4F00', '#FF5F00', '#FF6F00',
                  '#FF7F00', '#FF8F00', '#FF9F00', '#FFAF00',
                  '#FFBF00', '#FFCF00', '#FFDF00', '#FFEF00',
                  '#FFFF00', '#EFFF00', '#DFFF00', '#CFFF00',
                  '#BFFF00', '#AFFF00', '#9FFF00', '#8FFF00',
                  '#7FFF00', '#6FFF00', '#5FFF00', '#4FFF00',
                  '#3FFF00', '#2FFF00', '#1FFF00', '#0FFF00',
                  '#00FF00', '#00FF0F', '#00FF1F', '#00FF2F',
                  '#00FF3F', '#00FF4F', '#00FF5F', '#00FF6F',
                  '#00FF7F', '#00FF8F', '#00FF9F', '#00FFAF',
                  '#00FFBF', '#00FFCF', '#00FFDF', '#00FFEF',
                  '#00FFFF', '#00EFFF', '#00DFFF', '#00CFFF',
                  '#00BFFF', '#00AFFF', '#009FFF', '#008FFF',
                  '#007FFF', '#006FFF', '#005FFF', '#004FFF',
                  '#003FFF', '#002FFF', '#001FFF', '#000FFF',
                  '#0000FF', '#0F00FF', '#1F00FF', '#2F00FF',
                  '#3F00FF', '#4F00FF', '#5F00FF', '#6F00FF',
                  '#7F00FF', '#8F00FF', '#9F00FF', '#AF00FF',
                  '#BF00FF', '#CF00FF', '#DF00FF', '#EF00FF',
                  '#FF00FF', '#FF00EF', '#FF00DF', '#FF00CF',
                  '#FF00BF', '#FF00AF', '#FF009F', '#FF008F',
                  '#FF007F', '#FF006F', '#FF005F', '#FF004F',
                  '#FF003F', '#FF002F', '#FF001F', '#FF000F']

# Переменная для смены цвета
color_index = 0

# При изменении приоритетного направления движения все другие переменные
# для приоритещации движения обнуляются
while x <= size and x >= 0 and y <= size and y >= 0:
    if gravity_directions_options.get() == '🡸':
        w = gravity.get()
        n, s, e = 0, 0, 0
    elif gravity_directions_options.get() == '🡼':
        n, w = gravity.get(), gravity.get()
        s, e = 0, 0
    elif gravity_directions_options.get() == '🡹':
        n = gravity.get()
        s, e, w = 0, 0, 0
    elif gravity_directions_options.get() == '🡽':
        n, e = gravity.get(), gravity.get()
        s, w = 0, 0
    elif gravity_directions_options.get() == '🡺':
        e = gravity.get()
        n, s, w = 0, 0, 0
    elif gravity_directions_options.get() == '🡾':
        s, e = gravity.get(), gravity.get()
        n, w = 0, 0
    elif gravity_directions_options.get() == '🡻':
        s = gravity.get()
        n, e, w = 0, 0, 0
    elif gravity_directions_options.get() == '🡿':
        s, w = gravity.get(), gravity.get()
        n, e = 0, 0
    
    # Следующая точка будет нарисована в случайно выбранной близкой области
    # Приоритезация движения смещает границы выбора координат
    x += randint(-3 - w, 3 + e)
    y += randint(-3 - n, 3 + s)
    canvas.create_rectangle(x, y, x+7, y+7, 
                            fill=rainbow_colors[color_index % len(rainbow_colors)],
                            outline=rainbow_colors[color_index % len(rainbow_colors)])
    color_index += 1
    root.update()
    sleep(0.07)

root.mainloop()