import mon_module.Ai
import mon_module.Game
import unittest

class AITest(unittest.TestCase):



    def test_montecarloredux(self):
        jeu=game()
        li=[]
        for j in range(4):
            gj= game()
            gj.board=jeu.board
            gj.score=jeu.score
            if gj.playable(j):
                gj.play(j):
                    li.append(gj.board)
        play_move_simulation(jeu)
        self.assertIn(jeu.board,li)
        
    def test_montecarlo(self):
        jeu=game()
        li=[]
        for j in range(4):
            gj= game()
            gj.board=jeu.board
            gj.score=jeu.score
            if gj.playable(j):
                gj.play(j):
                    li.append(gj.board)
        play_monte_carlo(jeu)
        self.assertIn(jeu.board,li)
