# Программа запускает окно, в котором иллюстрируется работа клеточного автомата
# "Муревай Лэнгтона". В автомате используется тороидальная геометрия.
# В зависимости от размера клетки изменяется размер клеточного поля, т.е. 
# Более крупная клетка будет работать на более маленьком поле, в то время как
# мелкая клетка будет работать на большом поле. Муравей RL.


import tkinter


# Окно
root = tkinter.Tk()
root.title('Langton\'s ant')
root.configure(background='#FFFFFF')

# Область для рисования
size = 600
canvas = tkinter.Canvas(root, width=size, height=size, 
                        bg='#FFFFFF', highlightthickness=0)
canvas.pack()

# Создание таблицы, в которой будут записаны состояния клеток
dot_size = 5
grid_size = size // dot_size
matr = ['white'] * grid_size
for i in range(grid_size):
    matr[i] = ['white'] * grid_size
    
x = size // 2
y = size // 2

i = 0 # С помощью данной переменной будет проходить смена направления муравья
directions = ['n', 'e', 's', 'w']

current_direction = directions[i % len(directions)]
while True:
    if matr[(x//dot_size) % grid_size][(y//dot_size) % grid_size] == 'white':
        i += 1
        matr[(x//dot_size) % grid_size][(y//dot_size) % grid_size] = 'black'
        canvas.create_rectangle(x % size, y % size, (x + dot_size - 1) % size,
                                (y + dot_size - 1) % size, 
                                fill='#000000', outline='#000000')
    elif matr[(x//dot_size) % grid_size][(y//dot_size) % grid_size] == 'black':
        i -= 1
        matr[(x//dot_size) % grid_size][(y//dot_size) % grid_size] = 'white'
        canvas.create_rectangle(x % size, y % size, (x + dot_size - 1) % size,
                                (y + dot_size - 1) % size,
                                fill='#FFFFFF', outline='#FFFFFF')

    root.update()
    current_direction = directions[i % len(directions)]
    if current_direction == 'n':
        y -= 1 * dot_size
    elif current_direction == 'e':
        x += 1 * dot_size
    elif current_direction == 's':
        y += 1 * dot_size
    elif current_direction == 'w':
        x -= 1 * dot_size
    
root.mainloop()
