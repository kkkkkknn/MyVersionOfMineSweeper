import pygame
import constants
from player import Player
from game_map import GameMap
from end_screen import EndScreen
from health_bar import HealthBar
import menu
import mine1
import mine2
import mine3


def create_mines(level):
    mines = pygame.sprite.Group()

    if level == 1:
        x = constants.GAME_WIDTH // 2 - constants.CELL_SIZE
        y = constants.GAME_HEIGHT // 2 - constants.CELL_SIZE
        mine = mine1.Mine1(x, y)
        mines.add(mine)
    elif level == 2:
        x = constants.GAME_WIDTH // 2 - constants.CELL_SIZE
        y = constants.GAME_HEIGHT // 2 - constants.CELL_SIZE
        mine = mine2.Mine2(x, y)
        mines.add(mine)
    elif level == 3:
        x = constants.GAME_WIDTH // 2 - constants.CELL_SIZE
        y = constants.GAME_HEIGHT // 2 - constants.CELL_SIZE
        mine = mine3.Mine3(x, y)
        mines.add(mine)

    return mines

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    menu.display_menu()

    game_map = GameMap()
    player = Player()
    health_bar = HealthBar(player)
    level = 1
    mines = create_mines(level)

    end_screen = EndScreen()
    all_sprites = pygame.sprite.Group(game_map, player, health_bar, mines)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        all_sprites.update()
        health_bar.update()

        screen.fill(constants.BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
