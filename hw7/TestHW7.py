import unittest
import random
from HW7 import bubblesort, selectionsort, insertionsort, mergesort, quicksort

class TestSortingAlgorithms(unittest.TestCase):
    global instructions

    def setUp(self):
        # Reset instructions count before each test
        self.instructions = 0

    def test_bubblesort(self):
        self.run_sort_tests(bubblesort)

    def test_selectionsort(self):
        self.run_sort_tests(selectionsort)

    def test_insertionsort(self):
        self.run_sort_tests(insertionsort)

    def test_mergesort(self):
        self.run_sort_tests(mergesort)

    def test_quicksort(self):
        # Test cases for quicksort
        test_cases = [
            ([], []),
            ([1], [1]),
            ([4, 2], [2, 4]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            (random.sample(range(10), 10), sorted(random.sample(range(10), 10))),
            ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
            ([5, 3, 1, 2, 3, 1], [1, 1, 2, 3, 3, 5]),
        ]
        for arr, expected in test_cases:
            self.instructions = 0
            quicksort(arr, 0, len(arr) - 1)
            self.assertEqual(arr, expected)

    def run_sort_tests(self, sort_func):
        test_cases = [
            ([], []),
            ([1], [1]),
            ([4, 2], [2, 4]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            (random.sample(range(10), 10), sorted(random.sample(range(10), 10))),
            ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
            ([5, 3, 1, 2, 3, 1], [1, 1, 2, 3, 3, 5]),
        ]

        for original, expected in test_cases:
            arr = original[:]  # Make a copy of the array to sort
            if sort_func == quicksort:
                sort_func(arr, 0, len(arr) - 1)
            else:
                sort_func(arr)
            self.assertEqual(arr, expected)


if __name__ == '__main__':
    unittest.main()
