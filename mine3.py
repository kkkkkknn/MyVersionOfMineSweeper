import pygame

# from pygame.locals import *
from constants import *


class Mine3:
    def __init__(self):
        self.image = pygame.image.load('data/mine3.png')
        self.rect = self.image.get_rect()
        self.rect.x = 8 * TILE_SIZE
        self.rect.y = 8 * TILE_SIZE
        self.damage = 30
        self.visible = False

    def render(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)
