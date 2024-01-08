import pygame
import constants


class GameMap:
    def __init__(self, filename):
        self.map = self.load_map(filename)

    def load_map(self, filename):
        map = []
        with open(filename) as file:
            for line in file:
                row = []
                for char in line.strip():
                    row.append(char)
                map.append(row)
        return map

    def draw(self, screen):
        tile_size = constants.CELL_SIZE
        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == "G":
                    grass_image = pygame.image.load(constants.GRASS_IMAGE)
                    screen.blit(grass_image, (x * tile_size, y * tile_size))
