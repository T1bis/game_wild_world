import pygame
from random import *
class Prickle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(r'банан.png')
        self.show = 'off'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def locate_food(self):
        self.x = randint(0, 5) * 70 + 5
        self.y = randint(0, 5) * 70 + 5
