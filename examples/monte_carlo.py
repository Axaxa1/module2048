from module2048 import *
import random

jeu = Game2048()
while (not(jeu.gameover())):
    d = strategy_2048(jeu.game,jeu.state,jeu.moves)
    jeu.play(d)
    jeu.next_turn()
    print(jeu.game)


    



