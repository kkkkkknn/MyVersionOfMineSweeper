import pygame


class EndScreen:
    def __init__(self):
        self.image = pygame.image.load("data/end_game.png")

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
