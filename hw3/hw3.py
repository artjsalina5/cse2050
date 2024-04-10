import time
import random

def find_pairs_naive(L, n):
    """Finds pairs of numbers in a list that add up to a target value.

    This implementation uses a nested loop, resulting in O(n^2) time complexity.

    Args:
        L: The list of numbers to search.
        n: The target sum.

    Returns:
        set: A set of tuples, where each tuple represents a pair of numbers
             from the list that add up to the target value.
    """

    pairs = set()
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] + L[j] == n:
                pairs.add((L[i], L[j]))
    return pairs

def find_pairs_optimized(L, n):
    """Finds pairs of numbers in a list that add up to a target value.

    This implementation uses a dictionary for efficient lookups, resulting in
    O(n) time complexity.

    Args:
        L: The list of numbers to search.
        n: The target sum.

    Returns:
        set: A set of tuples, where each tuple represents a pair of numbers
             from the list that add up to the target value.
    """

    pairs = set()
    seen = {}
    for number in L:
        complement = n - number
        if complement in seen:
            # Ensure pairs are in sorted order for consistent output
            pairs.add((min(number, complement), max(number, complement)))
        seen[number] = True
    return pairs

def measure_min_time(func, args, n_trials=10):
    """Measures the minimum execution time of a function over multiple trials.

    Args:
        func: The function to be measured.
        args: A list or tuple of arguments to pass to the function.
        n_trials: The number of trials to run.

    Returns:
        float: The minimum execution time observed over all trials.
    """

    min_time = float('inf')
    for _ in range(n_trials):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        min_time = min(min_time, end - start)
    return min_time

def compare_algorithms():
    """Compares the performance of the naive and optimized pair-finding functions.
    """

    trials = [1800, 1850, 1950, 2150, 2500]
    print(f"n\tnaive\toptimized")
    for n in trials:
        list_to_test = generate_list(n)
        target = random.randint(1, n*10)

        # Reduce trials for naive due to high execution time with large inputs
        naive_time = measure_min_time(find_pairs_naive, [list_to_test, target], 10)
        optimized_time = measure_min_time(find_pairs_optimized, [list_to_test, target], 100)

        print(f"{n}\t{naive_time:.4f}\t{optimized_time:.4f}")

def generate_list(n):
    """Generates a list of n unique random numbers within a suitable range.

    Args:
        n: The desired length of the list.

    Returns:
        list: A list of n unique random numbers.
    """

    return random.sample(range(1, n*10), n)

if __name__ == "__main__":
    compare_algorithms()
