# bullet.py
import pygame
from settings import *


class PlayerBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    def update(self):
        self.y -= self.speed

    def is_off_screen(self):
        return self.y < 0

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x - 3, self.y - 10, 6, 14), border_radius=3)


class EnemyBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 6

    def update(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

    def hits_player(self, player):
        return abs(self.x - player.x) < 18 and abs(self.y - player.y) < 18

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x - 3, self.y, 6, 12), border_radius=3)
