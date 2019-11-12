import unittest
from module2048 import *
class AITest(unittest.TestCase):




    #On teste si im ne varie pas entre 2 essais pour être sur de faire le bon choixaa
    # !! Peut être faux !!
    def test_strat_2048(self):
        averages = [0,0,0,0]
        jeu = Game2048(numpy.array([[0,0,2,8],[0,0,2,4],[0,0,0,0],[0,0,0,0]]))
        for firstMove in range(4):
            for i in range(250):
                test = jeu.copy()
                if not(test.gameover()):
                    test.play(firstMove)
                    averages[firstMove] += playRandomModed(test,-1)/250
                
        im = 0
        for i in range(4):
            if averages[i] > averages[im]:
                im = i
        i2= strategy_2048(jeu.game,jeu.state,jeu.moves)
        self.assertEqual(i2,im)

    #Exemple
    # !! Peut aussi être FAUX !!
    def test_compute_score(self):
         jeu= Game2048()
         jeu.game = numpy.array([[0,0,2,8],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
         test= 0#valeuràtrouver
         i=computeScore(jeu)
         self.assertEqual(i,test)

        

if __name__== '__main__':
    unittest.main()
