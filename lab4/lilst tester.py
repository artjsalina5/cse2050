import unittest
from lister import Lister
from Queue import Queue

class ListerTester(unittest.TestCase):
    def test_div_by_5(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        lister = Lister(test_list)
        result = lister.div_by_5()

        self.assertEqual(result, [5, 10])


class QueueTester(unittest.TestCase):
    def test_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertFalse(queue.is_empty())
        self.assertEqual(len(queue), 2)


    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(8)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(len(queue), 1)
        with self.assertRaises(Exception):
            queue.dequeue()
            queue.dequeue()


    def test_firsttwo(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.firsttwo(), (1, 2))


    def test_firsttwo_insufficient(self):  # More descriptive name
        queue = Queue()
        queue.enqueue(1)  # Only one element added
        self.assertEqual(queue.firsttwo(), (-1, -1))  # Expect (-1, -1)


    def test_lasttwo(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.lasttwo(), (20, 30))

class StackTester(unittest.TestCase):
    def test_pop(self):
        """pop functionality in stack should remove and return the last element LIFO style"""
    def test_peek(self):
        """"peek functionality in stack should return top of stack without removal"""
    def test_push(self):
        """push functionality should add new element to the head"""


if __name__ == '__main__':
    unittest.main()
