def fib(n,fib_cache):
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n] = fib(n-1,fib_cache) + fib(n-2,fib_cache)
    return fib_cache[n]
fib_cache = {0: 1, 1: 1, 2: 2}
print(fib(7,fib_cache))
print(fib_cache)

def Fibonacci(n):
    f = []
    f.append(1)
    f.append(1)
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n], f
print(Fibonacci(7))

