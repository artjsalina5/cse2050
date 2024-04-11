import unittest
from waitlist import WaitList

class TestWaitList(unittest.TestCase):

    def setUp(self):
        self.waitlist = WaitList()
        # TODO: You may want to add some test data here for your tests.

    def test_add_customer(self):
        self.waitlist.add_customer('Alice', '10:00')
        self.waitlist.add_customer('Bob', '10:30')

        self.assertEqual(len(self.waitlist.pq), 2)

    def test_seat_customer(self):
        self.waitlist.add_customer('Alice', '10:00')
        self.waitlist.add_customer('Bob', '10:30')

        # Check the state of waitlist before seating customer
        self.assertEqual(len(self.waitlist.pq), 2)

        # Seat customer and check the state of waitlist after
        self.waitlist.seat_customer()
        self.assertEqual(len(self.waitlist.pq), 1)

    def test_peek_first_customer(self):
        self.waitlist.add_customer('Alice', '10:00')
        self.waitlist.add_customer('Bob', '10:30')

        # Call peek_next_customer and store its return value
        peeked_customer_message = self.waitlist.peek_next_customer()

        # Assert that the next customer on the waitlist is 'Alice'
        expected_message = "The next customer on the waitlist is: Alice, reservation time: 10:00"
        self.assertEqual(peeked_customer_message, expected_message)

if __name__ == '__main__':
    unittest.main()
