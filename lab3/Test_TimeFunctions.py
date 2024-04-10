from TimeFunctions import time_function

def test_func(L):
    """Multiplies each number in the list L by 2."""
    for i in range(len(L)):
        L[i] *= 2

def test_func_quadratic(L):
    """Performs a quadratic operation on the list L."""
    for i in range(len(L)):
        for j in range(len(L)):
            L[i] = L[i] * 2


# Testing with increasing sizes
sizes = [100, 1000, 1020, 1050, 1150]
for size in sizes:
    L = list(range(size))
    time_taken = time_function(test_func_quadratic, L)
    print(f"Size: {size}, Time taken: {time_taken * 1000:.3f} ms")