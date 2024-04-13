import unittest
from waitlist import WaitList


class TestWaitList(unittest.TestCase):

    def setUp(self):
        self.waitlist = WaitList()
        self.waitlist.add_customer('Alice', '10:00')
        self.waitlist.add_customer('Bob', '10:30')

    def test_add_customer(self):

        self.assertEqual(len(self.waitlist.pq), 2)

    def test_seat_customer(self):

        self.assertEqual(len(self.waitlist.pq), 2)

        self.waitlist.seat_customer()
        self.assertEqual(len(self.waitlist.pq), 1)

    def test_peek_first_customer(self):

        peeked_customer_message = self.waitlist.peek_next_customer()

        expected_message = "The next customer on the waitlist is: Alice, reservation time: 10:00"
        self.assertEqual(peeked_customer_message, expected_message)

    def test_change_reservation(self):
        changed_reservation = self.waitlist.change_reservation('Alice', '10:00', '10:30')
        expected_message = "Alice's reservation time has been changed to 10:30"
        self.assertEqual(changed_reservation, expected_message)


if __name__ == '__main__':
    unittest.main()
