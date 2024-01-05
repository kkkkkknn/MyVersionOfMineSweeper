import pygame
# import random
# import os
# import sys

intro_text = ["Это пародия  на классическую игру 'сапёр.'",
              "Всего у игрока 100 единиц здоровья.",
              "Есть мины 3 уровней:",
              "1 уровень -'Лепесток' наносит 25 урона",
              "2 уровень - 'Осколочная' наносит 50 урона",
              "3 уровень - 'Фугасная' наносит 100 урона",
              "Цель дойти до конца поля, пока вы живы."]


class StartGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height




if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Минные поля')
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((173, 255, 47))
        pygame.display.flip()
    pygame.quit()

