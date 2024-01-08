import pygame
import constants
from player import Player
from game_map import GameMap
from end_screen import EndScreen
from menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")

    clock = pygame.time.Clock()
    is_running = True

    menu = Menu()
    game_map = GameMap("data/map.txt")
    player = Player(game_map)

    current_screen = "menu"

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if current_screen == "menu":
                    if event.key == pygame.K_RETURN or event.button == 3:
                        current_screen = "game"
                elif current_screen == "game":
                    if event.key == pygame.K_ESCAPE:
                        current_screen = "menu"
                    elif event.key == pygame.K_w:
                        player.move("up")
                    elif event.key == pygame.K_s:
                        player.move("down")
                    elif event.key == pygame.K_a:
                        player.move("left")
                    elif event.key == pygame.K_d:
                        player.move("right")

        screen.fill(constants.BACKGROUND_COLOR)

        if current_screen == "menu":
            menu.draw(screen)
        elif current_screen == "game":
            game_map.draw(screen)
            player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
