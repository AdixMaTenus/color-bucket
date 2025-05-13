import unittest
from src.game.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_score(self):
        self.assertEqual(self.game.score, 0)

    def test_initial_lives(self):
        self.assertEqual(self.game.lives, 3)

    def test_score_increase(self):
        self.game.increase_score(1)
        self.assertEqual(self.game.score, 1)

    def test_life_decrease(self):
        self.game.decrease_life()
        self.assertEqual(self.game.lives, 2)

    def test_game_over(self):
        self.game.lives = 0
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()