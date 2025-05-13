import unittest
from src.game.bucket import Bucket
from src.utils.constants import COLORS

class TestBucket(unittest.TestCase):
    def setUp(self):
        self.bucket = Bucket()

    def test_move_left(self):
        initial_position = self.bucket.x
        self.bucket.move_left()
        self.assertLess(self.bucket.x, initial_position)

    def test_move_right(self):
        initial_position = self.bucket.x
        self.bucket.move_right()
        self.assertGreater(self.bucket.x, initial_position)

    def test_cycle_color(self):
        initial_color = self.bucket.color
        self.bucket.cycle_color()
        self.assertNotEqual(self.bucket.color, initial_color)

    def test_collision_with_ball(self):
        ball_color = COLORS['red']
        self.bucket.color = ball_color
        self.bucket.x = 100  # Assuming bucket's x position
        ball_position = (100, 50)  # Assuming ball's position
        self.assertTrue(self.bucket.check_collision(ball_position, ball_color))

if __name__ == '__main__':
    unittest.main()