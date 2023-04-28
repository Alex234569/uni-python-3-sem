import tkinter as tk
from time import sleep
from numpy import sign


class Car_Line:
    def __init__(self, number, color, length, distance, speed,
                 line, y_center, line_width):
        self.n = number # Количество машин в линии
        self.col = color # Цвет машины
        self.len = length # Длина машины
        self.dst = distance # Расстояние между машинами
        self.spd = speed # Скорость машины
        self.dir = sign(self.spd) # Направление движения машины
        self.lin = line # Номер полосы, по которой двигаются машины
        self.cnt = y_center # Координата центра экрана по y
        self.l_w = line_width # Ширина полосы
        self.wdt = (line_width // 2) - 5 # Половина ширины машины
        self.top = self.cnt - self.wdt + self.lin * self.l_w # Верхняя граница машины
        self.bot = self.cnt + self.wdt + self.lin * self.l_w # Нижняя граница машины
        # Следующая переменная нужна для того, чтобы определять, выехали ли
        # все машины за пределы экрана
        self.sta = -self.dir * (self.len * (self.n-1) + self.dst * (self.n-1))
        self.cars = [] # Список прямоугольников
        # Создание прямоугольников и добавление их в список
        for i in range(self.n):
            c = canvas.create_rectangle(self.sta + i * self.dst,
                                        self.top,
                                        self.len + self.sta + i * self.dst,
                                        self.bot,
                                        fill=self.col, outline='#000000')
            self.cars.append(c)
    
    # Проверка, пересекла ли машина границу экрана и её "отброс" назад в таком случае"
    # Также проверяет, не врезалась ли машина в игрока и "отбррос" его на начальную позицию в таком случае
    def check(self):
        
        if self.lin == current_line:
            for car in self.cars:
                if (canvas.coords(car)[0] < canvas.coords(player)[2] and canvas.coords(car)[2] > canvas.coords(player)[2] or
                    canvas.coords(car)[0] < canvas.coords(player)[0] and canvas.coords(car)[2] > canvas.coords(player)[0] or
                    canvas.coords(car)[0] < canvas.coords(player)[0] and canvas.coords(car)[2] > canvas.coords(player)[2]):
                    car_crash()
        
        if self.dir == 1:
            for car in self.cars:
                if canvas.coords(car)[0] > root.winfo_screenwidth():
                    canvas.coords(car, canvas.coords(car)[0] - root.winfo_screenwidth() - self.wdt - self.dst, self.top,
                                  canvas.coords(car)[2] - root.winfo_screenwidth() - self.wdt - self.dst, self.bot)
        elif self.dir == -1:
            for car in self.cars:
                if canvas.coords(car)[2] < 0:
                    canvas.coords(car, canvas.coords(car)[0] + root.winfo_screenwidth() + self.wdt + self.dst, self.top,
                                  canvas.coords(car)[2] + root.winfo_screenwidth() + self.wdt + self.dst, self.bot)


def close_window_esc(event):
    global running
    running = False

def close_window_default():
    global running
    running = False
    
def player_move_up(event):
    global current_line
    global line_width
    if current_line >= -3:
        current_line -= 1
        canvas.coords(player, canvas.coords(player)[0], canvas.coords(player)[1] - line_width,
                      canvas.coords(player)[2], canvas.coords(player)[3] - line_width)
    
def player_move_down(event):
    global current_line
    global line_width
    if current_line <= 3:
        current_line += 1
        canvas.coords(player, canvas.coords(player)[0], canvas.coords(player)[1] + line_width,
                      canvas.coords(player)[2], canvas.coords(player)[3] + line_width)
    
def car_crash():
    global current_line
    current_line = 4
    canvas.coords(player, x_center - player_half_width, y_center - player_half_width + current_line * line_width,
                  x_center + player_half_width, y_center + player_half_width + current_line * line_width)
                                    

# Параметры окна
root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>', close_window_esc)
root.protocol('WM_DELETE_WINDOW', close_window_default)

# Область рисования
left = 0
top = 0
right = root.winfo_screenwidth()
bot = root.winfo_screenheight()
canvas_width = right - left
canvas_height = bot - top
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height,
                   bg='#666666', highlightthickness=0)
canvas.pack(anchor='nw')

# Отрисовка фона
line_width = canvas_height // 10
half_line_width = line_width // 2
car_half_width = half_line_width - 5
x_center = canvas_width // 2
y_center = canvas_height // 2

for i in range(-3,4):
    canvas.create_rectangle(left, y_center - half_line_width + (i)*line_width, 
                            right, y_center + half_line_width + (i)*line_width,
                            fill='#999999', outline='#000000') 

# Отрисовка машин
car_lines = []
car_line_1 = Car_Line(2, '#00FF00', 500, 1000, -3, -3, y_center, line_width)
car_lines.append(car_line_1)
car_line_2 = Car_Line(4, '#FF0000', 200, 600, 10, -2, y_center, line_width)
car_lines.append(car_line_2)
car_line_3 = Car_Line(4, '#00FFFF', 100, 650, -5, -1, y_center, line_width)
car_lines.append(car_line_3)
car_line_4 = Car_Line(4, '#FFFF00', 150, 700, 20, 1, y_center, line_width)
car_lines.append(car_line_4)
car_line_5 = Car_Line(3, '#FF00FF', 350, 600, -5, 2, y_center, line_width)
car_lines.append(car_line_5)
car_line_6 = Car_Line(4, '#0000FF', 250, 600, 5, 3, y_center, line_width)
car_lines.append(car_line_6)
car_line_7 = Car_Line(4, '#0000FF', 250, 600, 5, 3, y_center, line_width)
car_lines.append(car_line_7)

# Отрисовка игрока
player_half_width = car_half_width
current_line = 4
player = canvas.create_rectangle(x_center - player_half_width, y_center - player_half_width + current_line * line_width,
                                 x_center + player_half_width, y_center + player_half_width + current_line * line_width,
                                 fill='#FFFFFF', outline='#000000')
root.bind('<Up>', player_move_up)
root.bind('<Down>', player_move_down)

running = True
while running:
    # Движение машин``
    for line in car_lines:
        for car in line.cars:
            canvas.move(car, line.spd, 0)
            line.check()
    
    # Обновление окна
    root.update()
    sleep(0.01)

root.destroy()
