# enemy.py
import pygame
import random
from settings import *


class Enemy:
    def __init__(self):
        self.x = random.randint(40, SCREEN_WIDTH - 40)
        self.y = -20
        self.hp = random.choice([1, 1, 2])  # 1 hp is more common
        self.dir = random.choice([-1, 1])   # horizontal direction
        self.shoot_cd = random.randint(60, 150)

    def update(self):
        # move down and sideways
        self.y += ENEMY_SPEED_Y
        self.x += self.dir * ENEMY_SPEED_X

        # bounce off walls
        if self.x < 20 or self.x > SCREEN_WIDTH - 20:
            self.dir *= -1

        self.shoot_cd -= 1

    def ready_to_shoot(self):
        if self.shoot_cd <= 0:
            self.shoot_cd = random.randint(80, 160)
            return True
        return False

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

    def hits_bullet(self, bullet):
        return abs(bullet.x - self.x) < 20 and abs(bullet.y - self.y) < 22

    def take_damage(self):
        self.hp -= 1

    def is_dead(self):
        return self.hp <= 0

    def draw(self, screen):
        x, y = int(self.x), int(self.y)
        # body
        pygame.draw.polygon(screen, RED, [(x, y+20), (x-18, y-10), (x+18, y-10)])
        # wings
        pygame.draw.polygon(screen, (160, 20, 20), [(x-18, y-10), (x-30, y-18), (x-10, y-3)])
        pygame.draw.polygon(screen, (160, 20, 20), [(x+18, y-10), (x+30, y-18), (x+10, y-3)])
        # center circle
        pygame.draw.circle(screen, YELLOW, (x, y+2), 6)
        # hp bar (only shown if hp > 1)
        if self.hp > 1:
            pygame.draw.rect(screen, GRAY, (x-18, y-28, 36, 5))
            pygame.draw.rect(screen, GREEN, (x-18, y-28, int(36 * self.hp / 3), 5))
