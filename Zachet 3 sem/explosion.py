import pygame

EXPLOSION_DURATION = 60 # Длительность взрыва в тиках
ANIMATION_CHANGE_DURATION = 10 # Период смены анимации

class Explosion:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.window = window
        self.textures = ('textures/explosion1.png', 'textures/explosion2.png')
        self.timeLeft = EXPLOSION_DURATION
        self.countAnimation = 0 - ANIMATION_CHANGE_DURATION // 2

    def draw(self):
        self.countAnimation += 1
        if self.countAnimation >= ANIMATION_CHANGE_DURATION // 2:
            self.countAnimation -= ANIMATION_CHANGE_DURATION
            self.explosionSurf = pygame.image.load(self.textures[0])
            self.explosionRect = self.explosionSurf.get_rect()
            self.explosionRect.center = (self.x, self.y)
        elif self.countAnimation <= 0:
            self.explosionSurf = pygame.image.load(self.textures[0])
            self.explosionRect = self.explosionSurf.get_rect()
            self.explosionRect.center = (self.x, self.y)
        elif self.countAnimation > 0:
            self.explosionSurf = pygame.image.load(self.textures[1])
            self.explosionRect = self.explosionSurf.get_rect()
            self.explosionRect.center = (self.x, self.y)
        self.timeLeft -= 1
        self.window.blit(self.explosionSurf, self.explosionRect)

    def check_out_of_time(self):
        if self.timeLeft <= 0:
            return True
        else:
            return False