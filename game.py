import pygame
# import sys
from pygame.locals import *
from constants import *
from player import Player
from game_map import GameMap
from menu import Menu
from end_screen import EndScreen
from health_bar import HealthBar
from mine1 import Mine1
from mine2 import Mine2
from mine3 import Mine3


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.menu = Menu()
        self.end_screen = EndScreen()
        self.health_bar = HealthBar()
        self.mine1 = Mine1()
        self.mine2 = Mine2()
        self.mine3 = Mine3()
        self.game_map = GameMap()
        self.player = Player(self.game_map, self.end_screen, self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_w:
                    self.player.move(0, -1)
                elif event.key == K_s:
                    self.player.move(0, 1)
                elif event.key == K_a:
                    self.player.move(-1, 0)
                elif event.key == K_d:
                    self.player.move(1, 0)

    def update(self):
        self.player.update()

        if self.player.rect.collidelist([self.mine1.rect, self.mine2.rect, self.mine3.rect]) != -1:
            self.player.hit()
            self.health_bar.update(self.player.health)

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.game_map.render(self.screen)
        self.player.render(self.screen)
        self.mine1.render(self.screen)
        self.mine2.render(self.screen)
        self.mine3.render(self.screen)

        # Отображение мин в зависимости от видимости игрока
        if self.player.visible:
            self.mine1.render(self.screen)
            self.mine2.render(self.screen)
            self.mine3.render(self.screen)
        self.health_bar.render(self.screen)
        pygame.display.flip()

    def run(self):
        self.menu.display(self.screen)
        self.mine1 = Mine1()
        self.mine2 = Mine2()
        self.mine3 = Mine3()
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
