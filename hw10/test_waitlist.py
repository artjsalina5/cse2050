import unittest
from waitlist import WaitList

class TestWaitList(unittest.TestCase):

    def setUp(self):
        self.waitlist = WaitList()
        # TODO: You may want to add some test data here for your tests.

    def test_add_customer(self):
        # TODO: Implement test for adding a customer.

    def test_seat_customer(self):
        # TODO: Implement test for seating a customer.

    def test_change_reservation_time(self):
        # TODO: Implement test for changing a reservation time.

    def test_peek_first_customer(self):
        # TODO: Implement test for peeking at the first customer.

    def test_print_reservation_list(self):
        # TODO: Implement test for printing the reservation list.

if __name__ == '__main__':
    unittest.main()
