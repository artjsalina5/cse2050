class Point:
    '''Class that defines a point in 2D space.'''
    def __init__(self, x, y):
        '''Assigns a point to this object with coordinates x and y.'''
        self.x = x
        self.y = y

    def __gt__(self, other):
        '''Compares one instanciated point to a nother using Greater Than Magic Method.'''
        return self.dist_from_origin() > other.dist_from_origin()

    def __lt__(self, other):
        '''Compares one instantiated point to another using the Less Than Magic Method.'''
        return self.dist_from_origin() < other.dist_from_origin()

    def __eq__(self, other):
        '''Compares one instantiated point to another using the Equals Magic Method.'''
        return self.dist_from_origin() == other.dist_from_origin()

    def __str__(self):
        '''Returns String representation of instantiated point.'''
        return f'Point({self.x}, {self.y})'

    def dist_from_origin(self):
        '''Calculates the straight line distance using Pythagorean Theorem.'''
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


if __name__ == '__main__':
    # Test points
    p1 = Point(3, 4)  # length = 5
    p2 = Point(8, 9)  # length > 5
    p3 = Point(-9, 7)    # length > 5
    p4 = Point(-2, 3)    # length < 5
    p5 = Point(9,-7)     # length > 5

    # Test initial coordinates
    assert p1.x == 3
    assert p1.y == 4

    # Tests for __gt__ method
    assert p3 > p4  # p3 is greater than p4 (True case)
    assert not p4 > p3  # p4 is not greater than p3 (False case)

    # Tests for __lt__ method
    assert p1 < p2  # p1 is less than p2 (True case)
    assert not p2 < p1  # p2 is not less than p1 (False case)

    # Tests for __eq__ method
    assert p3 == p5  # p3 is equal to p5 (True case)
    assert not p1 == p2  # p1 is not equal to p2 (False case)

    # Test __str__ method
    assert str(p1) == "Point(3, 4)"

    # Test dist_from_origin method
    assert p1.dist_from_origin() == 5.0 # p1 length is 5.0
    assert not p1.dist_from_origin() == 6.0 # p1 length is not 6.0