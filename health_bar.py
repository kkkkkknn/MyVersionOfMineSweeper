import pygame
import constants


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.Surface((100, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomright = (constants.SCREEN_WIDTH - 10, constants.SCREEN_HEIGHT - 10)

    def update(self):
        health_percentage = self.player.health / self.player.max_health
        health_width = int(health_percentage * self.image.get_width())

        self.image.fill((255, 0, 0))
        pygame.draw.rect(self.image, (0, 255, 0), (0, 0, health_width, self.image.get_height()))
