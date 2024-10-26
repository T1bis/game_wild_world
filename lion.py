import pygame
from random import *
class Lion():
    def __init__(self):
        self.image = pygame.image.load(r'lion.png')
        self.x = 5
        self.y = 5
        self.healt = 3
        self.velocity = 70

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def go_left(self):
        self.x -= self.velocity
        if self.x < 5:
            self.x = 5

    def go_right(self):
        self.x += self.velocity
        if self.x > 355:
            self.x = 355

    def go_up(self):
        self.y -= self.velocity
        if self.y < 5:
            self.y = 5

    def go_down(self):
        self.y += self.velocity
        if self.y > 355:
            self.y = 355

    def locate_food(self):
        old_x = self.x
        old_y = self.y
        self.x = randint(0, 5) * 70 + 5
        self.y = randint(0, 5) * 70 + 5
        while(old_y==self.y and old_x==self.x):
            self.x = randint(0, 5) * 70 + 5
            self.y = randint(0, 5) * 70 + 5
