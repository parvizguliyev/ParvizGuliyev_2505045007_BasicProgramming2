# menu.py
import pygame
import sys
import math
import random
from settings import *

# reuse the same stars list from here so menu also has background
stars = [[random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
          random.randint(1, 3), random.uniform(0.3, 1.5)] for _ in range(120)]


def draw_stars(screen):
    for s in stars:
        pygame.draw.circle(screen, (180, 180, 180), (int(s[0]), int(s[1])), s[2])
        s[1] += s[3]
        if s[1] > SCREEN_HEIGHT:
            s[1] = 0
            s[0] = random.randint(0, SCREEN_WIDTH)


def show_menu(screen, clock):
    font_big   = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 24)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # start game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

        screen.fill(DARK)
        draw_stars(screen)

        # pulsing title color
        t = pygame.time.get_ticks()
        pulse = int(150 + 100 * math.sin(t * 0.003))
        title = font_big.render(TITLE, True, (pulse, pulse, 255))
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 130))

        lines = [
            ("WASD  -  Move",           WHITE),
            ("SPACE  -  Shoot",         WHITE),
            (f"Destroy {KILL_GOAL} enemies to win", WHITE),
            ("",                        WHITE),
            ("Press ENTER to start",    YELLOW),
        ]
        for i, (text, color) in enumerate(lines):
            s = font_small.render(text, True, color)
            screen.blit(s, (SCREEN_WIDTH//2 - s.get_width()//2, 320 + i * 28))

        pygame.display.flip()


def show_end_screen(screen, clock, won, score, kills):
    font_big   = pygame.font.SysFont(None, 72)
    font_mid   = pygame.font.SysFont(None, 36)
    font_small = pygame.font.SysFont(None, 24)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True   # restart
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

        screen.fill(DARK)
        draw_stars(screen)

        msg   = "YOU WIN!" if won else "GAME OVER"
        color = YELLOW if won else RED
        s = font_big.render(msg, True, color)
        screen.blit(s, (SCREEN_WIDTH//2 - s.get_width()//2, 180))

        s2 = font_mid.render(f"Score: {score}    Kills: {kills}", True, WHITE)
        screen.blit(s2, (SCREEN_WIDTH//2 - s2.get_width()//2, 290))

        s3 = font_small.render("R - Restart      ESC - Quit", True, GRAY)
        screen.blit(s3, (SCREEN_WIDTH//2 - s3.get_width()//2, 380))

        pygame.display.flip()
