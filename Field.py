import pygame


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.field = [[0] * width for _ in range(height)]
        self.left = 290
        self.top = 10
        self.cell_size = 50

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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Минные поля')
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)

    board = Field(14, 14)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((173, 255, 47))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
