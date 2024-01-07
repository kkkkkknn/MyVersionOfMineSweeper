import sys

import pygame
from pygame.locals import *


class EndScreen:
    def __init__(self):
        self.background_image = pygame.image.load('data/end_game.png')

    def display(self, screen):
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(self.background_image, (0, 0))
            pygame.display.flip()
            clock.tick(30)
