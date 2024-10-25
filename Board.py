import time
from random import *
import pygame_menu
import pygame
from Button import Button

pygame.init()

window = pygame.display.set_mode((430, 430))
pygame.display.set_caption('Wild World')
menu = pygame_menu.Menu('Welcome', 430, 430,
                        theme=pygame_menu.themes.THEME_BLUE)






def start_menu():
    start = True
    while start:

        menu.add.text_input('Name :', default='Guest')
        menu.add.button('Play')

        menu.add.button('Quit', pygame_menu.events.EXIT)

        menu.mainloop(window)

        pygame.display.update()




