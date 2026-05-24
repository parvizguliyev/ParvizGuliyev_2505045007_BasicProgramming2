# main.py
# main place

import pygame
from settings import *
from menu import show_menu
from game import Game

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

show_menu(screen, clock)

game = Game(screen, clock)
while True:
    restart = game.run()
    if restart:
        game.reset()
    else:
        break

pygame.quit()
