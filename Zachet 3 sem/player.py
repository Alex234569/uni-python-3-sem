import math
import pygame

class Player:
    def __init__(self, screenWidth, screenHeight, window):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.window = window
        self.playerSurf = pygame.image.load('textures/playerIdle.png')
        self.width = self.playerSurf.get_width()
        self.height = self.playerSurf.get_height()
        self.x = self.screenWidth // 2
        self.y = self.screenHeight // 2
        self.angle = 0
        self.rotatedPlayerSurf = pygame.transform.rotate(self.playerSurf, self.angle)
        self.rotatedPlayerRect = self.rotatedPlayerSurf.get_rect()
        self.rotatedPlayerRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width // 2, self.y - self.sine * self.height // 2)
        self.invincibility = False

    def draw(self):
        self.window.blit(self.rotatedPlayerSurf, self.rotatedPlayerRect)

    # Пересчитывает значения угла наклона и переда корабля при движении
    def update_coords(self):
        self.rotatedPlayerSurf = pygame.transform.rotate(self.playerSurf, self.angle)
        self.rotatedPlayerRect = self.rotatedPlayerSurf.get_rect()
        self.rotatedPlayerRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width // 2, self.y - self.sine * self.height // 2)

    def turn_left(self):
        self.angle += 6
        self.update_coords()

    def turn_right(self):
        self.angle -= 6
        self.update_coords()

    def move_forvard(self):
        self.x += self.cosine * 8
        self.y -= self.sine * 8
        self.set_moving_sprite()

    # Обновление координат корабля, если он вышел за пределы экрана
    # e.g. корабль появится снизу, если полетел за верхнюю границу экрана
    def update_offscreen_location(self):
        if self.x >= self.screenWidth + self.width:
            self.x = 0
        elif self.x <= 0 - self.width:
            self.x = self.screenWidth
        elif self.y <= 0 - self.height:
            self.y = self.screenHeight
        elif self.y >= self.screenHeight + self.height:
            self.y = 0

    def set_moving_sprite(self):
        self.playerSurf = pygame.image.load('textures/playerMoving.png')
        self.update_coords()

    def set_idle_sprite(self):
        self.playerSurf = pygame.image.load('textures/playerIdle.png')
        self.update_coords()

    def move_to_center(self):
        self.x = self.screenWidth // 2
        self.y = self.screenHeight // 2
        self.angle = 0
