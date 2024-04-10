import unittest
def area(r=0):
    pi = 3.141592653589793
    return pi*r**2
class Test_area(unittest.TestCase):
    def test_accuracy(self):
        self.assertAlmostEqual(area(4), 50.265, 3)
if __name__ == '__main__':
    print(area(4))