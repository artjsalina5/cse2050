class Car:
    def __init__(self, a, b, c):
        self.make = a
        self.model = b
        self.year = c
    def __str__(self):
        return f'{self.make}, {self.model}, {self.year}'
class Complex:
    def __init__(self,a, b):
        self.real = a
        self.imag = b

    def __str__(self):
        if self.imag < 0:
            return f'{self.real}{self.imag}i'
        else:
            return f'{self.real}+{self.imag}i'

    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

class Polygon:
    def __init__(self, sides, points):
        self._sides  = sides
        self._points = list(points)
        if len(self._points) != sides:
            raise ValueError("Wrong number of points.")
    def sides(self):
        return self._sides

class Triangle(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 3, points)
    def __str__(self):
        return "I'm a triangle."

class PolygonCollection:
    def __init__(self):
        self._triangles = []
        self._squares = []

    def add(self, polygon):
        if polygon.sides() == 3:
            self._triangles.append(polygon)
        elif polygon.sides() == 4:
            self._squares.append(polygon)
    def __str__(self):
        return f"Triangles: {len(self._triangles)} \nSquares: {len(self._squares)}"
if __name__ == "__main__":
    c1 = Car("Dodge", "Caravan", 2005)
    print(c1)
    x = Complex(1,4)
    y = Complex(1, 4)
    print(x)
    print(x+y)
    print(x*y)
    c5 = PolygonCollection()
    print(c5)

import time
counter = 0
begin = time.time()
N = 5000
for i in range(N): # O(c * N*N) = O(cN^2), c is 'small' if you leave line 14 commented, but c is BIG if you uncomment it
    #print("i = %d" % i)
    #j = 1
    #while j < N: # O(log N)
    #    j *= 2
    for j in range(N): # O(N) inner loop, that will be repeated N times in the outer loop
        counter += 1 # this operation is O(1), and fast, let's say 0.0000000001 s
        # but if you uncomment the next line, the same algorithm will be noticeably much slower
        #print(" counter = %d" % counter) # this I/O operation is 'heavy', let's say 0.01s per statement...
print("counter = %d, computed in = %f" % (counter, time.time()-begin)) # elapsed time in seconds
# the default setup of this starting SpeedTest.py should be around 2-3s