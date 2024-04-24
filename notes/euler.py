def euler_method(f, x0, y0, h, n):
    x = x0
    y = y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
    return y

def dydx(x, y):
    return x * (y - 1)
i = 0
while i < 11:
    print(euler_method(dydx, 1, .5, .1, i))
    i += 1


