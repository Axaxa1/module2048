import unittest
from module2048 import *
class AITest(unittest.TestCase):



    def test_play_random_moveinfini(self):
        jeu = Game2048()
        playRandomModed(jeu,-1)
        self.assertTrue(jeu.gameover())
        
    def test_play_random_move(self):
        jeu=Game2048()
        n = 0
        for i in range(4):
            for j in range(4):
                if jeu.game[i][j] != 0:
                    n += 1
        playRandomModed(jeu,0)
        m = 0
        for i in range(4):
            for j in range(4):
                if jeu.game[i][j] != 0:
                    m += 1
        self.assertTrue(n + 1 == m)

    def test_play_random_moded(self):
        jeu = Game2048()
        res = playRandomModed(jeu)
        self.assertIsNotNone(res)
        self.assertTrue(res >= 0)

    def test_play_random_moded(self):
        jeu = Game2048()
        playRandomModed(jeu)
        res = progressiveScore(jeu)
        self.assertIsNotNone(res)
        self.assertTrue(res >= 0)
        

if __name__== '__main__':
    unittest.main()
