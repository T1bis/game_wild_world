import pygame
from food import Food
from lion import Lion
from random import *
from gameplay import *
import pygame_menu

FPS = 15

pygame.init()

window = pygame.display.set_mode((430, 430))
pygame.display.set_caption('Wild World')
window_menu = pygame.display.set_mode((430, 430))
pygame.display.set_caption('Wild World Menu')
menu = pygame_menu.Menu('Welcome', 430, 430,
                        theme=pygame_menu.themes.THEME_BLUE)


grases = pygame.image.load(r'grases.png')
f = pygame.font.SysFont('broadway', 20)
text = f.render("YUMMY!!!", True,
                  (128, 0, 0))

lion = Lion()

clock = pygame.time.Clock()

def made_flag_true(flag):
    flag = True

def made_flag_false(flag):
    flag = False

def wait_space(f_menu,f_game):

    while f_menu:
        clock.tick(FPS)

        menu.add.text_input('Name :', default='Guest')
        menu.add.button('Press Space to start',start(f_menu,f_game))
        menu.add.button('Quit', pygame_menu.events.EXIT)

        for event in pygame.event.get():
            print("Event_menu!")

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    wait_space(f_menu=True,f_game=False)
                    menu.mainloop(window)

                if event.key == pygame.K_SPACE:
                    start(f_menu=True,f_game=True)
                    menu.mainloop(window)
                    pygame.display.update()

        menu.mainloop(window)
        pygame.display.update()









def start(f_menu,f_game):
    foods_arr = []
    clock.tick(FPS)

    while f_game:
        window.fill((154, 205, 50))
        window.blit(grases, (0, 0))
        window.blit(lion.image, (lion.x, lion.y))
        make_arr(foods_arr, window, Food)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    wait_space(f_menu=True,f_game=False)

                if event.key == pygame.K_LEFT:
                    lion.go_left()
                    if infood(lion,foods_arr) ==1:
                        window.blit(text,(lion.x+20,lion.y+20))
                        pygame.display.update()

                if event.key == pygame.K_RIGHT:
                    lion.go_right()
                    if infood(lion, foods_arr) == 1:
                        window.blit(text, (lion.x - 30, lion.y - 20))
                        pygame.display.update()

                if event.key == pygame.K_UP:
                    lion.go_up()
                    if infood(lion, foods_arr) == 1:
                        window.blit(text, (lion.x - 20, lion.y - 30))
                        pygame.display.update()


                if event.key == pygame.K_DOWN:
                    lion.go_down()
                    if infood(lion, foods_arr) == 1:
                        window.blit(text, (lion.x - 20, lion.y + 30))
                        pygame.display.update()

                if event.key == pygame.K_SPACE:
                    start(f_menu=True,f_game=False)


            pygame.display.update()