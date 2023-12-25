import pygame

from PlayingField import PlayingField

# import random
# import os
# import sys

# from StartGame import StartGame

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Минные поля")
    size = width, height = 1600, 800
    screen = pygame.display.set_mode(size)

    board = PlayingField(18, 18)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((173, 255, 47))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
