import pygame


class HealthBar:
    def __init__(self):
        self.full_health = 100
        self.health = self.full_health
        self.width = 200
        self.height = 20

    def update(self, damage):
        self.health -= damage

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, self.width, self.height))
        health_width = int(self.health / self.full_health * self.width)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 10, health_width, self.height))
