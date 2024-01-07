import pygame

# from pygame.locals import *
from constants import *


class Mine2:
    def __init__(self):
        self.image = pygame.image.load('data/mine2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 5 * TILE_SIZE
        self.rect.y = 5 * TILE_SIZE
        self.damage = 20
        self.visible = False

    def render(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)
