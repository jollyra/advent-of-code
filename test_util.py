import unittest
from util import *


class TestStringMethods(unittest.TestCase):

    def test_X(self):
        point = (1, 2)
        self.assertEqual(X(point), 1)

    def test_Y(self):
        point = (1, 2)
        self.assertEqual(Y(point), 2)

    def test_manhattan_distance_whenPointsArePositive(self):
        p= (1, 1)
        q= (3, 3)
        self.assertEqual(manhattan_distance(p, q), 4)

    def test_manhattan_distance_whenPointsAreNegative(self):
        p= (-1, -1)
        q= (-3, -3)
        self.assertEqual(manhattan_distance(p, q), 4)

    def test_manhattan_distance_whenPointsArePositiveAndNegative(self):
        p= (-1, 1)
        q= (3, -3)
        self.assertEqual(manhattan_distance(p, q), 8)

    def test_neighbours4(self):
        p= (0, 0)
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.assertEqual(neighbours4(p), neighbours)

    def test_neighbours4_notOrigin(self):
        p= (1, 1)
        neighbours = [(2, 1), (1, 2), (0, 1), (1, 0)]
        self.assertEqual(neighbours4(p), neighbours)

    def test_neighbours8_notOrigin(self):
        p= (1, 1)
        neighbours = [(2, 1), (2, 2), (1, 2), (0, 2),
                (0, 1), (0, 0), (1, 0), (2, 0)]
        self.assertEqual(neighbours8(p), neighbours)

if __name__ == '__main__':
    unittest.main()
