import os
import sys

import pygame

FPS = 50


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Это пародия  на классическую игру 'сапёр.'",
                  "Всего у игрока 100 единиц здоровья.",
                  "Есть мины 3 уровней:",
                  "1 уровень -'Лепесток' наносит 25 урона",
                  "2 уровень - 'Осколочная' наносит 50 урона",
                  "3 уровень - 'Фугасная' наносит 100 урона",
                  "Цель дойти до конца поля, пока вы живы."]
    fon = pygame.transform.scale(load_image('fon.png'), (1280, 720))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


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
