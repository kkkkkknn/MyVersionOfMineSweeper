import pygame

# from pygame.locals import *
from constants import *


class HealthBar:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH - 220, SCREEN_HEIGHT - 50, 200, 20)
        self.health = 100

    def update(self, health):
        self.health = health

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        inner_rect = pygame.Rect(self.rect.x, self.rect.y, self.health * 2, self.rect.height)
        pygame.draw.rect(screen, (255, 0, 0), inner_rect)
