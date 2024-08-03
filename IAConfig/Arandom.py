from checkers.game import Game
import random

def agenteRandom(curretGame)-> Game:
    curretGame.move(random.choice(curretGame.get_possible_moves()))

def randVrand(curretGame)-> Game:
    try:
        while not curretGame.is_over():
            if curretGame.whose_turn() == 1:
                agenteRandom(curretGame)
            else:
                agenteRandom(curretGame)

    except KeyboardInterrupt:
        msg = "Juego Interrumpido!"
        return None
    return curretGame

if __name__ == "__main__":
    Newgame = Game()
    agenteRandom(Newgame)
    print((Newgame.get_possible_moves()))