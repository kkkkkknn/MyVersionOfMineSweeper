import pygame
import constants


class EndScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/end_game.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)

    def update(self):
        # Выводите дополнительное содержимое, например, поздравления или завершающее сообщение
        congratulation_text = "Поздравляем! Игра завершена!"
        font = pygame.font.Font(None, 30)
        text = font.render(congratulation_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))
        self.image.fill(constants.BACKGROUND_COLOR)
        self.image.blit(text, text_rect)
