import unittest
from LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_addfirst(self):
        """Test for adding a node to the beginning of a Linked List"""
        ll = LinkedList()
        ll.addfirst(1)
        self.assertEqual(repr(ll),"LinkedList(['1'])")

    def test_addlast(self):
        """Tests for adding a node to the end of a Linked List"""
        ll = LinkedList()
        ll.addlast(5)
        self.assertEqual(repr(ll), "LinkedList(['5'])")

    def test_removefirst(self):
        """Tests for removing the first node of a Linked List"""
        ll = LinkedList()
        ll.addfirst(1)
        ll.addfirst(2)
        removed_item = ll.removefirst()
        self.assertEqual(removed_item, 2)
        self.assertEqual(repr(ll), "LinkedList(['1'])")

        # Test removing from an empty list
        ll.removefirst()
        self.assertEqual(repr(ll), "LinkedList([])")
        self.assertIsNone(ll.removefirst())

    def test_removelast(self):
        """Tests removing the last node of a Linked List"""
        ll = LinkedList()
        ll.addfirst(1)
        ll.addfirst(2)
        removed_item = ll.removelast()
        self.assertEqual(removed_item, 1)
        self.assertEqual(repr(ll), "LinkedList(['2'])")

        # Test removing from an empty list
        ll.removelast()
        self.assertEqual(repr(ll), "LinkedList([])")
        self.assertIsNone(ll.removelast())

    def test_length(self):
        """Tests for the length of the Linked List"""
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        ll.addfirst(1)
        self.assertEqual(len(ll), 1)
        ll.addlast(2)
        self.assertEqual(len(ll), 2)
        ll.removefirst()
        self.assertEqual(len(ll), 1)
        ll.removelast()
        self.assertEqual(len(ll), 0)

    def test_str_and_repr_consistency(self):
        """Test to show consistent behavior of repr and str for the Linked List"""
        ll = LinkedList([1, 2, 3])
        expected_repr = "LinkedList(['1', '2', '3'])"
        self.assertEqual(repr(ll), expected_repr)
        expected_str = 'Your linked list contains: 1 ~and~ 2 ~and~ 3'
        self.assertEqual(str(ll), expected_str)


if __name__ == '__main__':
    unittest.main()
