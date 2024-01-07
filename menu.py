import pygame
import constants

def display_menu():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    background = pygame.image.load('data/fon.png').convert()

    rules_text = "Напишите правила вашей игры здесь"
    rules_font = pygame.font.Font(None, 30)
    text = rules_font.render(rules_text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        screen.blit(background, (0, 0))
        screen.blit(text, text_rect)
        pygame.display.update()
