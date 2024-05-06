import matplotlib.pyplot as plt
from main import startGame
from Arandom import randVrand

def graficarResultados(count:list,draws:list,B_win:list,W_win:list,label1:str,label2:str):
    loc = 'upper left'

    plt.ylabel("Resultados del juego en %")
    plt.xlabel("Número juegos")

    plt.plot(count, draws, 'r-', label = "Empate")
    plt.plot(count, W_win, 'g-', label = f"{label1} ganó")
    plt.plot(count, B_win, 'b-', label = f"{label2} ganó")

    plt.legend(loc = loc, shadow = True, fancybox=True, framealpha=0.7)

    plt.show()


def testVersus(numTests, versus : str):
    count = []
    draws = []
    B_win = []
    W_win = []
    for i in range(numTests):
        empate = 0
        win_Blanca = 0
        win_Negra= 0
        for _ in range(10):
            newGame = startGame()
            if (versus == "randVrand"): game = randVrand(newGame)
            if ( game.get_winner() is None): empate+=1
            if ( game.get_winner() == 2): win_Blanca+=1
            if ( game.get_winner() == 1): win_Negra+=1
        draws.append(empate)
        B_win.append(win_Blanca)
        W_win.append(win_Negra)
        count.append(i)
    graficarResultados(count, draws, B_win, W_win, "Blancas Random ganan","Negras Random ganan")

if __name__ == "__main__": 
    testVersus(50,"randVrand")