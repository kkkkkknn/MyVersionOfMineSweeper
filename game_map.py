import pygame
# from pygame.locals import *
from constants import *


class GameMap:
    def __init__(self, player):
        self.image = pygame.image.load('data/grass.png')
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - self.rect.width * TILE_COUNT) // 2
        self.rect.y = (SCREEN_HEIGHT - self.rect.height * TILE_COUNT) // 2
        self.player = player

    def render(self, screen):
        for x in range(self.rect.x, self.rect.x + self.rect.width * TILE_COUNT, self.rect.width):
            for y in range(self.rect.y, self.rect.y + self.rect.height * TILE_COUNT, self.rect.height):
                screen.blit(self.image, (x, y))
        self.player.render(screen)
