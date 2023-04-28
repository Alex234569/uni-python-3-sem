import random
import pygame

class Asteroid:
    def __init__(self, screenWidth, screenHeight, rank, window):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.rank = rank
        self.window = window
        if self.rank == 1:
            self.asteroidSurf = pygame.image.load('textures/asteroid1.png')
        elif self.rank == 2:
            self.asteroidSurf = pygame.image.load('textures/asteroid2.png')
        else:
            self.asteroidSurf = pygame.image.load('textures/asteroid3.png')
        self.asteroidRect = self.asteroidSurf.get_rect()
        self.width = self.asteroidSurf.get_width()
        self.height = self.asteroidSurf.get_height()
        self.startPoint = random.choice([
            (random.randrange(0, self.screenWidth - self.width),
             random.choice([-1 * self.height, self.screenHeight])), 
            (random.choice([-1 * self.width, self.screenWidth]),
             random.randrange(0, self.screenHeight - self.height))
             ])
        self.x, self.y = self.startPoint
        self.asteroidRect.center = (self.x, self.y)
        if self.x < self.screenWidth // 2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < self.screenHeight // 2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

    def move(self):
        self.x += self.xv
        self.y += self.yv
        self.asteroidRect.topleft = (self.x, self.y)

    def draw(self):
        self.window.blit(self.asteroidSurf, (self.x, self.y))

    def check_offscreen(self):
        if self.x < -self.width or self.x > self.screenWidth + self.width or self.y > self.screenHeight + self.height or self.y < -self.width:
            return True
        else:
            return False