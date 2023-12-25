import pygame


# import random
# import os
# import sys


class PlayingField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 410
        self.top = 13
        self.cell_size = 43

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(0, 100, 0), (x * self.cell_size + self.left,
                                                                   y * self.cell_size + self.top,
                                                                   self.cell_size, self.cell_size), 1)
