import sys

import pygame
from pygame.locals import *


class Menu:
    def __init__(self):
        self.background_image = pygame.image.load('data/fon.png')
        self.text = 'Rules: Move the character using W, A, S, D keys'

    def display(self, screen):
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        running = False

            screen.blit(self.background_image, (0, 0))
            screen.blit(text_render, text_rect)
            pygame.display.flip()
            clock.tick(30)
