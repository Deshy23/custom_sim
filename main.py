import pygame
import sys

# Initialize Pygame
pygame.init()

# Grid dimensions
GRID_SIZE = 10
CELL_SIZE = 40
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Set up the display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Gridworld")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_grid():
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        draw_grid()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
