import pygame
import random

GRID_COLS = 20
GRID_ROWS = 16
SQUARE_SIZE = 32
SCREEN_WIDTH = GRID_COLS * SQUARE_SIZE
SCREEN_HEIGHT = GRID_ROWS * SQUARE_SIZE

BACKGROUND_COLOR = (144, 238, 144)
LINE_COLOR = (0, 100, 0)

def draw_grid(screen):
    for x in range(0, SCREEN_WIDTH, SQUARE_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, SQUARE_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_WIDTH, y))


def move_mole():
    mole_x = random.randint(0, GRID_COLS - 1) * SQUARE_SIZE
    mole_y = random.randint(0, GRID_ROWS - 1) * SQUARE_SIZE
    return mole_x, mole_y


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (SQUARE_SIZE, SQUARE_SIZE))

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole Game")
        clock = pygame.time.Clock()


        mole_x, mole_y = move_mole()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + SQUARE_SIZE and mole_y <= mouse_y < mole_y + SQUARE_SIZE:
                        mole_x, mole_y = move_mole()

            screen.fill("light green")
            draw_grid(screen)

            screen.blit(mole_image, (mole_x, mole_y))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
