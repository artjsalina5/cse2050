# def fibonacci_naive(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# def fibonacci_memo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo) # Stores the number in a dictionary under key: n value: sum
#     return memo[n] # Dictionary call for the key that is your iterator for its value that is the sum
#
# def fibonacci_tab(n):
#     if n <= 1:
#         return n
#     fib_table = [0]*(n+1) # fib_table = [0, 0, ..., (n + 1)]
#     fib_table[1] = 1 # fib_table = [0, 1, 0, ..., (n + 1)]
#     for i in range(2, n+1):
#         fib_table[i] = fib_table[i-1] + fib_table[i-2] # fib_table = [ 0, 1, 1, 2, ... ]
#     return fib_table[n]

def lcs(X, Y):
    t = {}
    for i in range(len(X) + 1):
        t[(i, 0)] = ""
    for j in range(len(Y) + 1):
        t[(0, j)] = ""

    # Print initial state of t
    print("Initial t:")
    for key, value in sorted(t.items()):
        print(f"({key[0]}, {key[1]}) : {value}")
    print("\n")

    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                t[(i + 1, j + 1)] = t[(i, j)] + x
                print(f"Match found at i={i}, j={j}. Updated t:")
            else:
                t[(i + 1, j + 1)] = max([t[(i, j + 1)], t[(i + 1, j)]], key=len)
                print(f"No match at i={i}, j={j}. Updated t:")

            # Print updated t
            for key, value in sorted(t.items()):
                print(f"({key[0]}, {key[1]}) : {value}")
            print("\n")

    return t[(len(X), len(Y))]


# call to test function with parameters
lcs("ABCDE", "ACDFE")