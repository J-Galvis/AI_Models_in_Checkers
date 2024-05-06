import random

def agenteRandom(game):
    game.move(random.choice(game.get_possible_moves()))

def randVrand(game):
    try:
        while not game.is_over():
            if game.whose_turn() == 1:
                agenteRandom(game)
            else:
                agenteRandom(game)

    except KeyboardInterrupt:
        msg = "Juego Interrumpido!"
        return None
    return game