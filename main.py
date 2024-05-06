from checkers.game import Game
from Graphics import drawBoard
from Arandom import agenteRandom

def startGame():
    newGame = Game()
    newGame.board.player_turn = 2 #INICIA LA BLANCA
    return newGame

def createArray(game):
    Pieces = []
    for piece in game.board.pieces:
        # print(piece.king) #Me dice si es reina
        # print(piece.position) #Devuelve la posición en el tablero
        if piece.position == None: pass
        else : Pieces.append([piece.position,piece.player,piece.king,])
    Pieces.sort(key=lambda x: x[0])
    return Pieces

def evalGame(Pieces:list):
    P1 = []
    P2 = []
    for piece in Pieces:
        if piece[1] == 1: P2.append(piece)
        else: P1.append(piece)
    return P1,P2

if __name__ == "__main__": 
    # game = startGame()
    # Pieces = createArray(game)
    # P1,P2 = evalGame(Pieces)
    # print(P1)
    # drawBoard(Pieces)

    Newgame = startGame()
    for _ in range(30):agenteRandom(Newgame)
    Pieces = createArray(Newgame)
    P1,P2 = evalGame(Pieces)
    print(P1)
    drawBoard(Pieces)