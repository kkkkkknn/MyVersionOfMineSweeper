import pygame
import random

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FIELD_SIZE = 14
CELL_SIZE = int(SCREEN_HEIGHT / FIELD_SIZE)
BACKGROUND_COLOR = (173, 255, 47)
DATA_FOLDER = "data/"

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load images and sounds
grass_img = pygame.image.load(DATA_FOLDER + "grass.png")
solder_img = pygame.image.load(DATA_FOLDER + "solder.png")
fon_img = pygame.image.load(DATA_FOLDER + "fon.png")
end_game_img = pygame.image.load(DATA_FOLDER + "end_game.png")
mine_imgs = [pygame.image.load(DATA_FOLDER + "mine1.png"),
             pygame.image.load(DATA_FOLDER + "mine2.png"),
             pygame.image.load(DATA_FOLDER + "mine3.png")]
explosion_sound = pygame.mixer.Sound(DATA_FOLDER + "взрыв.wav")

# Game state variables
level_map = []
player_x = FIELD_SIZE // 2
player_y = FIELD_SIZE // 2
health = 100
mines = []
game_over = False


# Game class
class Game:
    def __init__(self):
        self.load_map()

    def load_map(self):
        with open(DATA_FOLDER + "map.txt", "r") as map_file:
            for line in map_file:
                level_map.append(line.strip())

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def draw_background(self):
        screen.fill(BACKGROUND_COLOR)

    def draw_field(self):
        for row in range(FIELD_SIZE):
            for col in range(FIELD_SIZE):
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                if level_map[row][col] == "#":
                    screen.blit(grass_img, (x, y))

    def draw_player(self):
        x = player_x * CELL_SIZE
        y = player_y * CELL_SIZE
        screen.blit(solder_img, (x, y))

    def draw_health_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (SCREEN_WIDTH - 120, SCREEN_HEIGHT - 40, health, 20))

    def draw_mines(self):
        for mine in mines:
            x = mine[0] * CELL_SIZE
            y = mine[1] * CELL_SIZE
            screen.blit(mine_imgs[mine[2]], (x, y))

    def draw_game_over(self):
        screen.blit(end_game_img, (0, 0))
        self.draw_text("GAME OVER", pygame.font.Font(None, 100), (255, 0, 0), SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2)

    def draw_congratulations(self):
        screen.blit(end_game_img, (0, 0))
        self.draw_text("CONGRATULATIONS!", pygame.font.Font(None, 80), (255, 255, 255), SCREEN_WIDTH / 2 - 300,
                       SCREEN_HEIGHT / 2 - 50)

    def handle_input(self):
        global player_x, player_y, health, game_over

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if player_y > 0:
                        player_y -= 1
                elif event.key == pygame.K_a:
                    if player_x > 0:
                        player_x -= 1
                elif event.key == pygame.K_s:
                    if player_y < FIELD_SIZE - 1:
                        player_y += 1
                elif event.key == pygame.K_d:
                    if player_x < FIELD_SIZE - 1:
                        player_x += 1

        for mine in mines:
            if player_x == mine[0] and player_y == mine[1]:
                health -= (mine[2] + 1) * 10
                explosion_sound.play()
                mines.remove(mine)

        if health <= 0:
            game_over = True

    def update(self):
        self.draw_background()
        if not game_over:
            self.draw_field()
            self.draw_player()
            self.draw_health_bar()
            self.draw_mines()
        else:
            self.draw_game_over()

        pygame.display.flip()
        clock.tick(60)


# Main game loop
def main():
    game = Game()

    # Home screen
    screen.blit(fon_img, (0, 0))
    game.draw_text("RULES:", pygame.font.Font(None, 50), (0, 0, 0), 100, 100)
    
