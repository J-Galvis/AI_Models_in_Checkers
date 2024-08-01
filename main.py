import pygame
from setup import *

pygame.init()

listPositions = []
# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Rectangle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        self.x = x
        self.y = y
        self.number = None
        self.Playable = False if (self.x + self.y) % 2 == 0 else True
        self.color = BLACK if self.Playable else WHITE

        if self.Playable:
            if self.y == 0: self.number = (self.x + 1)//2
            else: self.number = ((self.y * 4) + (self.x)//2) +1
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Board')

def create_board()-> None:
    for row in range(ROWS):
        for col in range(COLS):
            listPositions.append(Rectangle(col, row))

def draw_board(screen)-> None:
    for position in listPositions:
        position.draw(screen)


def initGame() -> None:
    clock = pygame.time.Clock()
    clock.tick(60)
    create_board()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for position in listPositions:
                    if position.is_clicked(pygame.mouse.get_pos()):
                        print(position.number)

        draw_board(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    initGame()
