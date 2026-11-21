import unittest

from Duck import Duck


class DuckTests(unittest.TestCase):
    def test_starts_at_origin(self):
        self.assertEqual(Duck("Donald").position, (0, 0))

    def test_moves_in_each_direction(self):
        duck = Duck("Donald")
        self.assertEqual(duck.move("forward"), (0, 1))
        self.assertEqual(duck.move("right"), (1, 1))
        self.assertEqual(duck.move("backward"), (1, 0))
        self.assertEqual(duck.move("left"), (0, 0))

    def test_unknown_direction_raises(self):
        with self.assertRaises(ValueError):
            Duck("Donald").move("up")


if __name__ == "__main__":
    unittest.main()
