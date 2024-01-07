import pygame

# from pygame.locals import *
from constants import *


class Mine1:
    def __init__(self):
        self.image = pygame.image.load('data/mine1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 3 * TILE_SIZE
        self.rect.y = 3 * TILE_SIZE
        self.damage = 10
        self.visible = False

    def render(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)
