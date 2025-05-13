import unittest
from src.game.ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.ball = Ball()

    def test_spawn_ball(self):
        self.ball.spawn()
        self.assertIsNotNone(self.ball.position)
        self.assertIn(self.ball.color, self.ball.available_colors)

    def test_falling_behavior(self):
        initial_position = self.ball.position[1]
        self.ball.update()
        self.assertGreater(self.ball.position[1], initial_position)

    def test_catch_ball(self):
        self.ball.spawn()
        bucket_position = (self.ball.position[0], self.ball.position[1] + 50)  # Simulate bucket position
        caught = self.ball.check_catch(bucket_position)
        self.assertTrue(caught)

if __name__ == '__main__':
    unittest.main()