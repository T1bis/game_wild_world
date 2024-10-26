import pygame
from food import Food
from lion import Lion
from game import Prickle
from Board import Menu
from random import *
from gameplay import *
import pygame as pg

if __name__=='__main__':
    FPS = 10

    pygame.init()

    window = pygame.display.set_mode((430, 430))
    menu = Menu(75, 35)
    buttons = menu.get_buttons()
    pygame.display.set_caption('Wild World')
    grases = pygame.image.load(r'grases.png')
    menu_im = pygame.image.load(r'menu.png')
    f = pygame.font.SysFont('broadway', 20)
    text = f.render("YUMMY!!!", True,
                    (128, 0, 0))

    lion = Lion()

    clock = pygame.time.Clock()

    foods_arr = []
    joke_arr = []

    f_menu = True
    f_game = False
    while True:
        clock.tick(FPS)
        if f_menu is True:
            window.blit(grases, (0, 0))
            window.blit(menu_im, (190,160))
            menu.show_menu(window,menu.get_buttons())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        loadorno = button.is_triggered(event.pos, menu)
                        if loadorno is not None:
                            if loadorno == 'endgame':
                                pygame.quit()
                                quit()
                            if loadorno == 'play':
                                f_menu = False
                                f_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        f_menu = False
                        f_game = True

        elif f_menu is False and f_game is True:
            window.fill((154, 205, 50))
            window.blit(grases, (0, 0))
            window.blit(lion.image, (lion.x, lion.y))
            arr = make_arr(foods_arr, window, Food,2,lion)
            arr1 = make_arr(joke_arr, window, Prickle,randint(1,2),lion)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        f_menu = True
                        f_game = False

                    elif event.key == pygame.K_LEFT:
                        lion.go_left()
                        if in_one_place(lion, foods_arr) == 1:
                            window.blit(text, (lion.x + 20, lion.y + 20))
                            pygame.display.update()
                        if in_joke(lion, joke_arr) == 1:
                            pygame.display.update()

                    elif event.key == pygame.K_RIGHT:
                        lion.go_right()
                        if in_one_place(lion, foods_arr) == 1:
                            window.blit(text, (lion.x - 30, lion.y - 20))
                            pygame.display.update()
                        if in_joke(lion, joke_arr) == 1:
                            pygame.display.update()

                    elif event.key == pygame.K_UP:
                        lion.go_up()
                        if in_one_place(lion, foods_arr) == 1:
                            window.blit(text, (lion.x - 20, lion.y - 30))
                            pygame.display.update()
                        if in_joke(lion, joke_arr) == 1:
                            pygame.display.update()

                    elif event.key == pygame.K_DOWN:
                        lion.go_down()
                        if in_one_place(lion, foods_arr) == 1:
                            window.blit(text, (lion.x - 20, lion.y + 30))
                            pygame.display.update()
                        if in_joke(lion, joke_arr) == 1:
                            pygame.display.update()

        pygame.display.update()














