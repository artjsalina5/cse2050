import unittest, random
from BSTMap import BSTMap


class TestBSTMap(unittest.TestCase):
    def test_equal_empty(self):
        """
        Tests the equality of two empty MyBSTMap instances.

        Syntax: test_equal_empty()
        Arguments: None
        Output: Asserts that two empty MyBSTMap instances are equal.
        """
        bst1 = BSTMap()
        bst2 = BSTMap()
        self.assertEqual(bst1, bst2, "Two empty MyBSTMap instances should be equal.")

    def test_equal_multiplenodes(self):
        """
        Tests the equality of two MyBSTMap instances with identical key-value pairs.

        Syntax: test_equal_multiplenodes()
        Arguments: None
        Output: Asserts that two MyBSTMap instances with the same key-value pairs are equal.
        """
        # Create the first MyBSTMap instance and add multiple key-value pairs
        bst1 = BSTMap()
        bst1.put(3, 'Three')
        bst1.put(1, 'One')
        bst1.put(4, 'Four')
        bst1.put(2, 'Two')

        # Create the second MyBSTMap instance and add the same key-value pairs in the same order
        bst2 = BSTMap()
        bst2.put(3, 'Three')
        bst2.put(1, 'One')
        bst2.put(4, 'Four')
        bst2.put(2, 'Two')

        # Assert that the two instances are considered equal
        self.assertEqual(bst1, bst2, "Two MyBSTMap instances with identical nodes should be equal.")

    def test_notequal_multiplenodes_difshapes(self):
        """
        Tests the inequality of two MyBSTMap instances with the same keys and values but different structures.

        Syntax: test_notequal_multiplenodes_difshapes()
        Arguments: None
        Output: Asserts that two structurally different MyBSTMap instances are not equal.
        """
        # Create the first MyBSTMap instance and add nodes in a specific order
        bst1 = BSTMap()
        bst1.put(4, 'Four')
        bst1.put(2, 'Two')  # Adding in a way that '2' becomes a left child
        bst1.put(6, 'Six')
        bst1.put(1, 'One')  # Further nesting to define a specific tree shape

        # Create the second MyBSTMap instance and add the same nodes but in a different order
        bst2 = BSTMap()
        bst2.put(4, 'Four')
        bst2.put(6, 'Six')  # Adding in a way that '6' is directly a right child
        bst2.put(2, 'Two')  # Changing the structure compared to bst1
        bst2.put(1, 'One')  # Same value and key but the structure leading here is different

        # Assert that the two instances are considered not equal
        self.assertNotEqual(bst1, bst2,
                            "Two MyBSTMap instances with identical nodes but different structures should not be equal.")

    def test_notequal_multiplenodes_difkvs(self):
        """
        Tests the inequality of two MyBSTMap instances with different key-value pairs.

        Syntax: test_notequal_multiplenodes_difkvs()
        Arguments: None
        Output: Asserts that two MyBSTMap instances with different key-value pairs are not equal.
        """
        bst1 = BSTMap()
        bst1.put(1, 'One')

        bst2 = BSTMap()
        bst2.put(1, 'Two')  # same key but different value compared to bst1

        self.assertNotEqual(bst1, bst2, "Two MyBSTMap instances with different key-value pairs should not be equal.")

    # def test_frompreorder_small(self):
    #     """
    #     Tests constructing a small MyBSTMap instance from a preorder sequence.
    #
    #     Syntax: test_frompreorder_small()
    #     Arguments: None
    #     Output: Validates the MyBSTMap instance constructed from a small preorder sequence.
    #     """
    #     preorder_list = [(4, 'Four'), (2, 'Two'), (1, 'One'), (3, 'Three'), (5, 'Five')]
    #
    #     # Use this preorder sequence to create a MyBSTMap instance
    #     bst_from_preorder = BSTMap.frompreorder(preorder_list)
    #
    #     # Now create a similar tree manually to compare
    #     expected_bst = BSTMap()
    #     expected_bst.put(4, 'Four')
    #     expected_bst.put(2, 'Two')
    #     expected_bst.put(1, 'One')
    #     expected_bst.put(3, 'Three')
    #     expected_bst.put(5, 'Five')
    #
    #     # Assert that the BST created from the preorder sequence is equal to the manually created BST
    #     self.assertEqual(bst_from_preorder, expected_bst,
    #                      "The BST constructed from the provided preorder sequence does not match the expected BST.")
    #
    # def test_frompreorder_large(self):
    #     """
    #     Tests constructing a large MyBSTMap instance from a preorder sequence.
    #
    #     Syntax: test_frompreorder_large()
    #     Arguments: None
    #     Output: Validates the MyBSTMap instance constructed from a large preorder sequence.
    #     """
    #     preorder_list = [(50, 'Fifty'), (30, 'Thirty'), (20, 'Twenty'),
    #                      (40, 'Forty'), (70, 'Seventy'), (60, 'Sixty'),
    #                      (80, 'Eighty'), (75, 'Seventy Five'), (90, 'Ninety')]
    #
    #     # Use this preorder sequence to create a MyBSTMap instance
    #     bst_from_preorder = BSTMap.frompreorder(preorder_list)
    #
    #     # Now create a similar tree manually to compare
    #     expected_bst = BSTMap()
    #     for kv_pair in preorder_list:
    #         expected_bst.put(kv_pair[0], kv_pair[1])
    #
    #     # Assert that the BST created from the preorder sequence is equal to the manually created BST
    #     self.assertEqual(bst_from_preorder, expected_bst,
    #                      "The BST constructed from the large preorder sequence does not match the expected BST.")
    #
    # def test_frompostorder_small(self):
    #     """
    #     Tests constructing a small MyBSTMap instance from a postorder sequence.
    #
    #     Syntax: test_frompostorder_small()
    #     Arguments: None
    #     Output: Validates the MyBSTMap instance constructed from a small postorder sequence.
    #     """
    #     postorder_list = [(1, 'One'), (3, 'Three'), (2, 'Two'), (5, 'Five'), (4, 'Four')]
    #
    #     bst_from_postorder = BSTMap.frompostorder(postorder_list)
    #
    #     expected_bst = BSTMap()
    #     for kv in [(4, 'Four'), (2, 'Two'), (1, 'One'), (3, 'Three'),
    #                (5, 'Five')]:  # This preorder sequence would result in the same tree as the postorder list above
    #         expected_bst.put(kv[0], kv[1])
    #
    #     self.assertEqual(bst_from_postorder, expected_bst,
    #                      "The BST constructed from the provided small postorder sequence does not match the expected BST.")
    #
    # def test_frompostorder_large(self):
    #     """
    #     Tests constructing a large MyBSTMap instance from a postorder sequence.
    #
    #     Syntax: test_frompostorder_large()
    #     Arguments: None
    #     Output: Validates the MyBSTMap instance constructed from a large postorder sequence.
    #     """
    #     postorder_list = [(20, 'Twenty'), (40, 'Forty'), (30, 'Thirty'), (60, 'Sixty'), (90, 'Ninety'), (80, 'Eighty'),
    #                       (70, 'Seventy'), (50, 'Fifty')]
    #
    #     bst_from_postorder = BSTMap.frompostorder(postorder_list)
    #
    #     expected_bst = BSTMap()
    #     for kv in [(50, 'Fifty'), (30, 'Thirty'), (20, 'Twenty'), (40, 'Forty'), (70, 'Seventy'), (60, 'Sixty'),
    #                (80, 'Eighty'), (90, 'Ninety')]:  # A preorder sequence that would build the same tree
    #         expected_bst.put(kv[0], kv[1])
    #
    #     self.assertEqual(bst_from_postorder, expected_bst,
    #                      "The BST constructed from the provided large postorder sequence does not match the expected BST.")
    #


if __name__ == '__main__':
    unittest.main()
