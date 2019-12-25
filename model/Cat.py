import pygame


class Cat:
    GROUND_LEVEL = 330
    GRAVITY = 0.5
    CAT_IMG = pygame.image.load('image/cat.png')

    def __init__(self, display, x, y, vx, vy):
        self.display = display
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.vy += self.GRAVITY
        self.x += self.vx
        self.y += self.vy
        if self.y > self.GROUND_LEVEL:
            self.y = self.GROUND_LEVEL
            self.vy = 0
        if self.x < -self.CAT_IMG.get_width():
            self.x = self.display.get_width() + self.CAT_IMG.get_width()
        if self.x > self.display.get_width() + self.CAT_IMG.get_width():
            self.x = -self.CAT_IMG.get_width()

    def jump(self):
        self.vy = -15

    def draw(self):
        self.display.blit(self.CAT_IMG, (self.x, self.y))