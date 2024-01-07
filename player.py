import pygame

# from pygame.locals import *
from constants import *


class Player:
    def __init__(self, game_map, end_screen, screen):
        self.image = pygame.image.load('data/solder.png')
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2
        self.rect.y = (SCREEN_HEIGHT - self.rect.height) // 2
        self.health = 100
        self.visible = False
        self.game_map = game_map
        self.end_screen = end_screen
        self.screen = screen

    def move(self, dx, dy):
        self.rect.x += dx * TILE_SIZE
        self.rect.y += dy * TILE_SIZE

    def update(self):
        if self.rect.left < self.game_map.rect.x:
            self.rect.left = self.game_map.rect.x
        elif self.rect.right > self.game_map.rect.x + self.game_map.rect.width * TILE_COUNT:
            self.rect.right = self.game_map.rect.x + self.game_map.rect.width * TILE_COUNT
        if self.rect.top < self.game_map.rect.y:
            self.rect.top = self.game_map.rect.y
        elif self.rect.bottom > self.game_map.rect.y + self.game_map.rect.height * TILE_COUNT:
            self.rect.bottom = self.game_map.rect.y + self.game_map.rect.height * TILE_COUNT

    def hit(self):
        self.health -= 10
        if self.health <= 0:
            self.health = 0
            self.visible = False
            self.end_screen.display(self.screen)

    def render(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)
