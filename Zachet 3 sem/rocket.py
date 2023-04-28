import pygame

class Rocket:
    def __init__(self, player, screenWidth, screenHeight, window):
        self.startPoint = player.head
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.window = window
        self.x, self.y = self.startPoint
        self.angle = player.angle
        self.cosine = player.cosine
        self.sine = player.sine
        self.rocketSurf = pygame.image.load('textures/rocket.png')
        self.rotatedRocketSurf = pygame.transform.rotate(self.rocketSurf, self.angle)
        self.rotatedRocketRect = self.rotatedRocketSurf.get_rect()
        self.rotatedRocketRect.center = (self.x, self.y)
        self.xv = self.cosine * 12
        self.yv = self.sine * 12

    def move(self):
        self.x += self.xv
        self.y -= self.yv
        self.rotatedRocketRect.center = (self.x, self.y)

    def draw(self):
        self.window.blit(self.rotatedRocketSurf, self.rotatedRocketRect)

    def check_offscreen(self):
        if self.x < -50 or self.x > self.screenWidth or self.y > self.screenHeight or self.y < -50:
            return True
        else:
            return False
