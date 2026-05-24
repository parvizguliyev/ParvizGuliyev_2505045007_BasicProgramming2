# game.py
import pygame
import sys
from settings import *
from player import Player
from enemy import Enemy
from bullet import PlayerBullet, EnemyBullet
from menu import draw_stars, show_end_screen


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font_mid   = pygame.font.SysFont(None, 36)
        self.font_small = pygame.font.SysFont(None, 24)
        self.reset()

    def reset(self):
        self.player = Player()
        self.enemies = []
        self.player_bullets = []
        self.enemy_bullets = []
        self.score = 0
        self.kills = 0
        self.spawn_timer = 0

    def run(self):
        while True:
            self.clock.tick(FPS)
            self._handle_events()
            self._update()
            self._draw()

            # check end conditions
            if self.player.is_dead():
                pygame.time.wait(800)
                restart = show_end_screen(self.screen, self.clock, False, self.score, self.kills)
                return restart

            if self.kills >= KILL_GOAL:
                pygame.time.wait(800)
                restart = show_end_screen(self.screen, self.clock, True, self.score, self.kills)
                return restart

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

    def _update(self):
        keys = pygame.key.get_pressed()

        # player movement
        self.player.handle_input(keys)

        # player shooting
        if self.player.can_shoot(keys):
            self.player_bullets.append(PlayerBullet(self.player.x, self.player.y - 25))

        # update player bullets
        for b in self.player_bullets[:]:
            b.update()
            if b.is_off_screen():
                self.player_bullets.remove(b)

        # update enemy bullets
        for eb in self.enemy_bullets[:]:
            eb.update()
            if eb.is_off_screen():
                self.enemy_bullets.remove(eb)
                continue
            if eb.hits_player(self.player):
                self.enemy_bullets.remove(eb)
                self.player.take_damage()

        # spawn enemies
        self.spawn_timer += 1
        if self.spawn_timer >= SPAWN_RATE:
            self.enemies.append(Enemy())
            self.spawn_timer = 0

        # update enemies
        for e in self.enemies[:]:
            e.update()

            # enemy reached the bottom
            if e.is_off_screen():
                self.enemies.remove(e)
                self.player.take_damage()
                continue

            # enemy shooting
            if e.ready_to_shoot():
                self.enemy_bullets.append(EnemyBullet(e.x, e.y + 20))

            # check collision with player bullets
            for b in self.player_bullets[:]:
                if e.hits_bullet(b):
                    self.player_bullets.remove(b)
                    e.take_damage()
                    if e.is_dead():
                        self.score += 100
                        self.kills += 1
                        if e in self.enemies:
                            self.enemies.remove(e)
                    break

    def _draw(self):
        self.screen.fill(DARK)
        draw_stars(self.screen)

        for e in self.enemies:
            e.draw(self.screen)

        for b in self.player_bullets:
            b.draw(self.screen)

        for eb in self.enemy_bullets:
            eb.draw(self.screen)

        self.player.draw(self.screen)
        self._draw_hud()
        pygame.display.flip()

    def _draw_hud(self):
        # top bar background
        pygame.draw.rect(self.screen, (15, 15, 40), (0, 0, SCREEN_WIDTH, 38))
        pygame.draw.line(self.screen, BLUE, (0, 38), (SCREEN_WIDTH, 38), 1)

        # hp hearts
        hp_text = self.font_small.render("HP:", True, WHITE)
        self.screen.blit(hp_text, (8, 10))
        for i in range(self.player.hp):
            pygame.draw.circle(self.screen, RED, (45 + i * 22, 19), 8)

        # score
        sc = self.font_mid.render(f"Score: {self.score}", True, YELLOW)
        self.screen.blit(sc, (SCREEN_WIDTH//2 - sc.get_width()//2, 6))

        # kills
        kl = self.font_small.render(f"Kills: {self.kills}/{KILL_GOAL}", True, GRAY)
        self.screen.blit(kl, (SCREEN_WIDTH - 110, 10))
