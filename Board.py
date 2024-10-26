import pygame
from Button import Button

class Menu:
    def __init__(self,weight,height):
        self.quit = Button(105,305,"Quit")
        self.play = Button(105,105,"Play")
        self.status = 'on'
        self.weight = weight
        self.height = height
        self.font = pygame.font.SysFont('broadway', 40)

    def get_buttons(self):
        self.buttons = []

        self.buttons = [self.play, self.quit]

        return self.buttons

    def set_status(self, new):
        self.status = new

    def get_status(self):
        return self.status

    def show_menu(self, screen, buttons):
        for button in buttons:
            button.draw(screen)

        screen.blit(self.font.render("Menu", True, (0, 71, 49)),(self.weight+20, self.height))