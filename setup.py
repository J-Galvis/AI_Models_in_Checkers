from checkers.game import Game
from Arandom import agenteRandom

# Constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
LIGHT_COLOR = (255, 230, 120)
DARK_COLOR = (60, 40, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def startGame()-> Game:
    newGame = Game()
    newGame.board.player_turn = 2
    return newGame

def createArray(game)-> list:
    listPieces = [] 
    for piece in game.board.pieces:
        if piece.position == None: pass
        else : listPieces.append([piece.position,piece.player,piece.king,])
    return listPieces

def evalGame(listPieces:list)-> list:
    P1 = []
    P2 = []
    for piece in listPieces:
        if piece[1] == 1: P2.append(piece)
        else: P1.append(piece)
    return P1,P2

def mainSetUp()-> None:
    Newgame = startGame()
    # for _ in range(30): agenteRandom(Newgame)
    listPieces = createArray(Newgame)
    P1,P2 = evalGame(listPieces)
    print(P1,P2)

if __name__ == "__main__": 
    mainSetUp()