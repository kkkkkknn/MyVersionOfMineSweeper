import pygame
import constants


class Menu:
    def __init__(self):
        self.background_image = pygame.image.load(constants.FON_IMAGE)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
