import unittest

from Game import GuessingGame, MAX_NUMBER, MIN_NUMBER


class GuessingGameTests(unittest.TestCase):
    def test_secret_number_is_in_range(self):
        for _ in range(100):
            game = GuessingGame()
            self.assertTrue(MIN_NUMBER <= game.secret_number <= MAX_NUMBER)

    def test_hints(self):
        game = GuessingGame(secret_number=50)
        self.assertEqual(game.check_guess(10), "low")
        self.assertEqual(game.check_guess(90), "high")
        self.assertEqual(game.check_guess(50), "correct")

    def test_attempts_are_counted(self):
        game = GuessingGame(secret_number=50)
        game.check_guess(1)
        game.check_guess(2)
        game.check_guess(50)
        self.assertEqual(game.attempts, 3)


if __name__ == "__main__":
    unittest.main()
