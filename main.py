import pygame

pygame.init()

listPositions = []
# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Board')

def draw_board(screen)-> None:
    counter=0
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            listPositions.append([counter,row,col])

def verPosiciones(pos: tuple[int,int])-> int:
    ...



def initGame() -> None:
    clock = pygame.time.Clock()
    clock.tick(60)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

        draw_board(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    initGame()
