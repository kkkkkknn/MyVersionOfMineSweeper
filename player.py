import pygame
import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, game_map):
        super().__init__()
        self.image = pygame.image.load(constants.PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.game_map = game_map

    def move(self, direction):
        if direction == "up":
            new_x, new_y = self.rect.x, self.rect.y - constants.CELL_SIZE
        elif direction == "down":
            new_x, new_y = self.rect.x, self.rect.y + constants.CELL_SIZE
        elif direction == "left":
            new_x, new_y = self.rect.x - constants.CELL_SIZE, self.rect.y
        elif direction == "right":
            new_x, new_y = self.rect.x + constants.CELL_SIZE, self.rect.y

        # Проверка, доступна ли целевая клетка для перемещения
        if self.game_map.is_tile_walkable(new_x, new_y):
            self.rect.x = new_x
            self.rect.y = new_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

