import pygame
from setup import *

pygame.init()

listPositions = []

class SquareBoard:
    def __init__(self, x, y)-> None:
        self.rect = pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        self.x = x
        self.y = y
        self.number = None
        self.Playable = False if (self.x + self.y) % 2 == 0 else True
        self.color = DARK_COLOR if self.Playable else LIGHT_COLOR

        if self.Playable:
            if self.y == 0: self.number = (self.x + 1)//2
            else: self.number = ((self.y * 4) + (self.x)//2) +1
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def is_clicked(self, pos)-> bool:
        return self.rect.collidepoint(pos)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Board')

def create_board()-> None:
    for row in range(ROWS):
        for col in range(COLS):
            listPositions.append(SquareBoard(col, row))

def draw_board(screen)-> None:
    for position in listPositions:
        position.draw(screen)


def draw_pieces(screen, listPositions:list ,listPieces:list)-> None:

    piece_dict = {piece[0]: piece for piece in listPieces} 
    '''
    This creates a dictionary where the keys is the number of the piece
    and the values are the corresponding pieces.
    '''

    for position in listPositions:
        piece = piece_dict.get(position.number)
        if piece:
            if piece[1] == 1: color=WHITE
            else: color=BLACK
            pygame.draw.circle(screen, color, pygame.Rect(position.x*SQUARE_SIZE, position.y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE).center, 22)

    

def initGame() -> None:
    clock = pygame.time.Clock()
    clock.tick(60)
    create_board()

    run = True

    Newgame = startGame()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for position in listPositions:
                    if position.is_clicked(pygame.mouse.get_pos()):
                        print(position.number)
        
        agenteRandom(Newgame)

        listPieces = createArray(Newgame)
        draw_board(screen)
        draw_pieces(screen, listPositions, listPieces)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    initGame()
