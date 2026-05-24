# player.py
import pygame
import random
from settings import *


class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 80
        self.hp = PLAYER_MAX_HP
        self.speed = PLAYER_SPEED
        self.bullet_cooldown = 0

    def handle_input(self, keys):
        # move with WASD
        if keys[pygame.K_a]: self.x -= self.speed
        if keys[pygame.K_d]: self.x += self.speed
        if keys[pygame.K_w]: self.y -= self.speed
        if keys[pygame.K_s]: self.y += self.speed

        # clamp to screen
        self.x = max(25, min(SCREEN_WIDTH - 25, self.x))
        self.y = max(45, min(SCREEN_HEIGHT - 45, self.y))

    def can_shoot(self, keys):
        # returns True if player pressed space and cooldown is done
        self.bullet_cooldown -= 1
        if keys[pygame.K_SPACE] and self.bullet_cooldown <= 0:
            self.bullet_cooldown = BULLET_COOLDOWN
            return True
        return False

    def take_damage(self):
        self.hp -= 1

    def is_dead(self):
        return self.hp <= 0

    def draw(self, screen):
        x, y = self.x, self.y
        # body
        pygame.draw.polygon(screen, BLUE, [(x, y-28), (x-16, y+18), (x+16, y+18)])
        # wings
        pygame.draw.polygon(screen, CYAN, [(x-16, y+8), (x-34, y+22), (x-8, y+2)])
        pygame.draw.polygon(screen, CYAN, [(x+16, y+8), (x+34, y+22), (x+8, y+2)])
        # cockpit
        pygame.draw.circle(screen, (180, 230, 255), (x, y-8), 7)
        # engine flame - random height so it flickers
        fh = random.randint(8, 20)
        pygame.draw.polygon(screen, ORANGE, [(x-6, y+18), (x+6, y+18), (x, y+18+fh)])
        pygame.draw.polygon(screen, YELLOW, [(x-3, y+18), (x+3, y+18), (x, y+18+fh//2)])
