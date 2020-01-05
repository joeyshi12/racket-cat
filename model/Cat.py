import pygame


class Cat:
    GROUND_LEVEL: int = 330
    GRAVITY: float = 0.4
    CAT_IMG = pygame.image.load('image/cat.png')
    jumping = False

    def __init__(self, display, x, y):
        self.display = display
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def move(self):
        """updates cat state for next frame"""
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
        if self.jumping and self.y == self.GROUND_LEVEL:
            self.vy = -12

    def draw(self):
        """draws cat image on display"""
        self.display.blit(self.CAT_IMG, (self.x, self.y))
