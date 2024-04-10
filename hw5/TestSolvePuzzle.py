import unittest
from solve_puzzle import solve_puzzle

class TestSolvePuzzle(unittest.TestCase):
    """Tests for the solve_puzzle function."""
    def test_clockwise_solvable(self):
        """Tests a board configuration solvable with clockwise jumps only."""
        board = [1, 2, 1, 0]
        solvable, moves = solve_puzzle(board)
        self.assertTrue(solvable)
        self.assertEqual(moves, [0, 1, 3])

    def test_counterclockwise_solvable(self):
        """Tests a board configuration solvable with counterclockwise jumps only."""
        board = [1, 3, 0, 2]
        solvable, moves = solve_puzzle(board)
        self.assertTrue(solvable)
        self.assertEqual(moves, [0, 3])  # Expected moves if solvable counter-clockwise only

    def test_mixed_solvable(self):
        """Tests a board configuration requiring a mix of clockwise and counterclockwise jumps."""
        board = [3, 1, 2, 1, 0]  # Requires a mixture of movements
        solvable, moves = solve_puzzle(board)
        self.assertTrue(solvable)
        self.assertEqual(moves, [0, 3, 4])


    def test_unsolvable(self):
        """Tests a board configuration that has no solution."""
        board = [2, 1, 1, 2, 0]  # Example unsolvable board
        solvable, moves = solve_puzzle(board)
        self.assertFalse(solvable)

if __name__ == '__main__':
    unittest.main()