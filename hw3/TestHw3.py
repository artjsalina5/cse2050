import unittest
from hw3 import find_pairs_naive, find_pairs_optimized

class TestPairFindingAlgorithms(unittest.TestCase):

    def test_basic_functionality(self):
        """Using a basic list, test hw3"""
        self.assertEqual(find_pairs_naive([1, 2, 3, 4, 5], 5), {(1, 4), (2, 3)})
        self.assertEqual(find_pairs_optimized([1, 2, 3, 4, 5], 5), {(1, 4), (2, 3)})

    def test_with_negative_numbers(self):
        """Using a list with negative numbers"""
        self.assertEqual(find_pairs_naive([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 0), {(-5, 5), (-4, 4), (-3, 3), (-2, 2), (-1, 1)})
        self.assertEqual(find_pairs_optimized([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 0), {(-5, 5), (-4, 4), (-3, 3), (-2, 2), (-1, 1)})

    def test_no_pairs(self):
        """Using a list and target where no two numbers can sum up to the target"""
        self.assertEqual(find_pairs_naive([1, 2, 3, 4], 10), set())
        self.assertEqual(find_pairs_optimized([1, 2, 3, 4], 10), set())

    def test_large_list(self):
        """Using a somewhat large list"""
        large_list = list(range(100))
        target = 50
        expected_pairs = {(10, 40), (11, 39), (1, 49), (2, 48), (18, 32), (17, 33), (8, 42), (24, 26), (9, 41), (15, 35), (0, 50), (16, 34), (19, 31), (6, 44), (22, 28), (7, 43), (23, 27), (14, 36), (5, 45), (13, 37), (20, 30), (21, 29), (12, 38), (3, 47), (4, 46)}
        self.assertEqual(find_pairs_naive(large_list, target), expected_pairs)
        self.assertEqual(find_pairs_optimized(large_list, target), expected_pairs)


if __name__ == '__main__':
    unittest.main()
