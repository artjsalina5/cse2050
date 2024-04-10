class HappyNumber():
    def __init__(self, number):
        self.number = number

    def num2list(self, n):
        """Recursively Converts any integer n into a list of single-digit integers"""
        if n == 0:
            return []
        else:
            return self.num2list(n // 10) + [n % 10]

    def num2list2(self, n):
        """Non-Recursively converts any integer n into
        a list of single-digit integers"""
        digits = []
        while n > 0:
            digits.insert(0, n % 10)  # Insert digits at the beginning for correct order
            n //= 10
        return digits

    def sum_of_squares(self, L):
        """Calculates the sum of squares for use in ishappy"""
        total = 0
        for num in L:
            total += num ** 2
        return total

    def ishappy(self, n, seen=None):
        """Outputs True of number is Happy (1) or False if number is Not Happy"""
        if seen is None:  # Create a set if not already created
            seen = set()

        if n == 1:
            return True
        if n in seen:
            return False

        seen.add(n)  # Ok, next
        next_sum = self.sum_of_squares(self.num2list(n))  # Feed in from recursive list
        return self.ishappy(next_sum, seen)

    def isprime(self, n):
        def does_divide(a, b):
            # Returns True if b is divisible by a
            return b % a == 0

        def smooth(k):
            return (k >= 2) and ((does_divide(k, n)) or smooth(k-1))

        return not smooth(int(n ** 0.5))

    def happy_prime(self, n):
        """Returns True if the number is both a prime and a happy number, otherwise False"""
        return self.isprime(n) and self.ishappy(n)

    def next_happy_prime(self, n, n_attempts=0):
        """Finds the next highest happy-prime number after 'n'. If 'n_attempts' of prime numbers is reached, returns False."""
        n += 1  # Start checking from the next number after 'n'
        while n_attempts > 0:
            if self.isprime(n) and self.ishappy(n):
                return n
            n += 1
            n_attempts -= 1
        return False
