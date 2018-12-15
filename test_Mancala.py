import unittest
from Mancala import Mancala
from Human_Player import Human_Player

class Test_Mancala(unittest.TestCase):
    def test_mancal(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        self.assertEqual(mancala.starting_stones, 3)
        self.assertEqual(mancala.starting_holes, 6)

    def test_reset(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        self.assertEqual(mancala.player_1_holes, [3, 3, 3, 3, 3, 3])
        self.assertEqual(mancala.player_2_holes, [3, 3, 3, 3, 3, 3])
        self.assertEqual(mancala.player_1_mancala, 0)
        self.assertEqual(mancala.player_2_mancala, 0)
        self.assertEqual(mancala.turn, 1)
