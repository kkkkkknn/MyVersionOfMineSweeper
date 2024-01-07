import pygame
import constants


class GameMap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((constants.GAME_WIDTH, constants.GAME_HEIGHT))
        self.image.fill(constants.BACKGROUND_COLOR)

        grass_image = pygame.image.load('data/grass.png').convert_alpha()
        grass_image = pygame.transform.scale(grass_image, (constants.CELL_SIZE, constants.CELL_SIZE))

        for x in range(0, constants.GAME_WIDTH, constants.CELL_SIZE):
            for y in range(0, constants.GAME_HEIGHT, constants.CELL_SIZE):
                self.image.blit(grass_image, (x, y))

        self.rect = self.image.get_rect()
        self.rect.center = (constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
