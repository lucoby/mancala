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

    def test_valid_move_pos(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        self.assertTrue(mancala.valid_move(0))
        self.assertTrue(mancala.valid_move(1))
        self.assertTrue(mancala.valid_move(5))
        self.assertFalse(mancala.valid_move(-1))
        self.assertFalse(mancala.valid_move(6))
        self.assertFalse(mancala.valid_move(7))

    def test_valid_move_zero_stones(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        mancala.player_1_holes[2] = 0
        self.assertTrue(mancala.valid_move(1))
        self.assertTrue(mancala.valid_move(3))
        self.assertFalse(mancala.valid_move(2))
        mancala.turn = 2
        self.assertTrue(mancala.valid_move(1))
        self.assertTrue(mancala.valid_move(3))
        self.assertTrue(mancala.valid_move(2))
        mancala.player_2_holes[2] = 0
        self.assertTrue(mancala.valid_move(1))
        self.assertTrue(mancala.valid_move(3))
        self.assertFalse(mancala.valid_move(2))

    def test_mancala(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        self.assertFalse(mancala.valid_mancala(0))
        mancala.player_1_holes[0] = 1
        self.assertTrue(mancala.valid_mancala(0))
        mancala.player_1_holes[1] = 2
        self.assertTrue(mancala.valid_mancala(1))
        mancala.player_1_holes[1] = 5
        self.assertFalse(mancala.valid_mancala(1))
        mancala.player_1_holes[2] = 16
        self.assertTrue(mancala.valid_mancala(2))
        mancala.turn = 2
        mancala.player_2_holes[2] = 3
        self.assertTrue(mancala.valid_mancala(2))

    def test_apply_move_no_mancala(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        mancala.apply_move(4)
        self.assertEqual(mancala.player_1_mancala, 0)
        self.assertEqual(mancala.player_2_mancala, 0)
        self.assertEqual(mancala.player_1_holes, [3, 4, 4, 4, 0, 3])
        self.assertEqual(mancala.player_2_holes, [3, 3, 3, 3, 3, 3])
        self.assertEqual(mancala.turn, 2)

    def test_apply_move_mancala(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        mancala.apply_move(2)
        self.assertEqual(mancala.player_1_mancala, 1)
        self.assertEqual(mancala.player_2_mancala, 0)
        self.assertEqual(mancala.player_1_holes, [4, 4, 0, 3, 3, 3])
        self.assertEqual(mancala.player_2_holes, [3, 3, 3, 3, 3, 3])
        self.assertEqual(mancala.turn, 1)

    def test_apply_move_add_to_opponent(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        mancala.apply_move(0)
        self.assertEqual(mancala.player_1_mancala, 1)
        self.assertEqual(mancala.player_2_mancala, 0)
        self.assertEqual(mancala.player_1_holes, [0, 3, 3, 3, 3, 3])
        self.assertEqual(mancala.player_2_holes, [3, 3, 3, 3, 4, 4])
        self.assertEqual(mancala.turn, 2)

    def test_apply_move_add_to_opponent_p2(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        mancala.turn = 2
        mancala.apply_move(0)
        self.assertEqual(mancala.player_1_mancala, 0)
        self.assertEqual(mancala.player_2_mancala, 1)
        self.assertEqual(mancala.player_1_holes, [3, 3, 3, 3, 4, 4])
        self.assertEqual(mancala.player_2_holes, [0, 3, 3, 3, 3, 3])
        self.assertEqual(mancala.turn, 1)

    def test_apply_move_big_move(self):
        mancala = Mancala(Human_Player(), Human_Player(), starting_stones=3, starting_holes=6)
        mancala.reset()
        mancala.player_1_holes[1] = 15
        mancala.apply_move(1)
        self.assertEqual(mancala.player_1_mancala, 2)
        self.assertEqual(mancala.player_2_mancala, 0)
        self.assertEqual(mancala.player_1_holes, [5, 1, 4, 4, 4, 4])
        self.assertEqual(mancala.player_2_holes, [4, 4, 4, 4, 4, 4])
        self.assertEqual(mancala.turn, 1)
