import pygame
import constants


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/soldier.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (constants.GAME_WIDTH // 2, constants.GAME_HEIGHT // 2)
        self.velocity = constants.CELL_SIZE

    def update(self, keys):
        dx = dy = 0
        if keys[pygame.K_w]:
            dy -= self.velocity
        elif keys[pygame.K_s]:
            dy += self.velocity
        elif keys[pygame.K_a]:
            dx -= self.velocity
        elif keys[pygame.K_d]:
            dx += self.velocity

        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        if 0 <= new_x < constants.GAME_WIDTH - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y < constants.GAME_HEIGHT - self.rect.height:
            self.rect.y = new_y
