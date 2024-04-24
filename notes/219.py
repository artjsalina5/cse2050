def f(k):
    if k > 0:
        return f(k-1) + k
    return 0
def fib(k):
    if k in [0,1]: return k
    return fib(k-1) + fib(k-2)

def fib_better(k):
    def fib_helper(k, n, F_minus_1, F_minus_2):
        if n == k:
            return F_minus_1
        return fib_helper(k, n+1, F_minus_1 + F_minus_2, F_minus_1)
    return fib_helper(k, 2, 1, 1)
def fib_direct(k):
    return ((((1+5**5)/2)**k)%10**9+5)%10
print(fib_direct(50))


L = [1,2,3,4,5,6,7,8,9]
L[0] = L[-1]
print(L)
L.pop()
print(L)
