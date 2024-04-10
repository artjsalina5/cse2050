import unittest
from lab5 import HappyNumber
class TestHappyNumber(unittest.TestCase):
    """Tests for HappyNumber methods."""
    def setUp(self):
        """Setup method to create an instance of HappyNumber."""
        self.happy_number = HappyNumber(1)

    def test_num2list(self):
        """Tests recursive conversion of integer to list of digits.
        Input: Integer, Output: List of integers."""
        result = self.happy_number.num2list(123)
        self.assertEqual(result, [1, 2, 3])

    def test_num2list2(self):
        """Tests non-recursive conversion of integer to list of digits.
        Input: Integer, Output: List of integers."""
        result = self.happy_number.num2list2(123)
        self.assertEqual(result, [1, 2, 3])

    def test_sum_of_squares(self):
        """Tests sum of squares of list elements.
        Input: List of integers, Output: Integer."""
        result = self.happy_number.sum_of_squares([1, 2, 3])
        self.assertEqual(result, 14)

    def test_ishappy(self):
        """Tests if a number is happy.
        Input: Integer, Output: Boolean."""
        result = self.happy_number.ishappy(19)
        self.assertTrue(result)

    def test_isprime(self):
        """Tests if a number is prime.
        Input: Integer, Output: Boolean."""
        result = self.happy_number.isprime(5)
        self.assertTrue(result)

    def test_happy_prime(self):
        """Tests if a number is both happy and prime.
        Input: Integer, Output: Boolean."""
        result = self.happy_number.happy_prime(7)
        self.assertTrue(result)
    def test_next_happy_prime(self):
        """Tests finding the next happy prime after a number within a set number of attempts.
        Input: Integer (n), Integer (n_attempts), Output: Integer or False."""
        # Test case 1: Find the next happy prime after 7 with sufficient attempts
        expected_next_happy_prime = 13
        result = self.happy_number.next_happy_prime(7, 10)
        self.assertEqual(result, expected_next_happy_prime, "The next happy prime after 7 should be 13.")

        # Test case 2: Test for a scenario where n_attempts limit is reached without finding a next happy prime
        result = self.happy_number.next_happy_prime(7, 1)  # Only 1 attempt, not enough to find the next happy prime
        self.assertFalse(result, "Should return False if the n_attempts limit is reached without finding a next happy prime.")
if __name__ == '__main__':
    unittest.main()