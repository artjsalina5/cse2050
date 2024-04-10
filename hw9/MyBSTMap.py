from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    def __eq__(self, other):
        """
        Compares two MyBSTMap instances for equality.

        Syntax: __eq__(self, other)
        Arguments:
            - other: Another MyBSTMap instance to compare with.

        Output: True if the two MyBSTMap instances have identical tree structures
                and corresponding key-value pairs, False otherwise.
        """
             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.
        if not isinstance(other, MyBSTMap):
            return False
        return self.root == other.root


    # these are "static" methods - they belong to the class but do not take an instance of
    # the class as a parameter (no `self``).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod
    def frompreorder(L):
        """
        Constructs a MyBSTMap from a given preorder sequence.

        Syntax: frompreorder(L)
        Arguments:
            - L: A list of key-value tuples in preorder traversal order.

        Output: A new MyBSTMap instance populated with the key-value pairs from the preorder sequence.
        """
        new_bst = MyBSTMap()
        for key_value in L:
            new_bst.put(key_value[0], key_value[1])
        return new_bst

    @staticmethod
    def frompostorder(L):
        """
        Constructs a MyBSTMap from a given postorder sequence.

        Syntax: frompostorder(L)
        Arguments:
            - L: A list of key-value tuples in postorder traversal order.

        Output: A new MyBSTMap instance populated with the key-value pairs from the postorder sequence.
        """
        new_bst = MyBSTMap()
        for key_value in reversed(L):
            new_bst.put(key_value[0], key_value[1])
        return new_bst


class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    def __eq__(self, other):
        """
        Compares two MyBSTNode instances for equality.

        Syntax: __eq__(self, other)
        Arguments:
            - other: Another MyBSTNode instance to compare with.

        Output: True if the two MyBSTNode instances have the same key, value,
                and subtree structure, False otherwise.
        """
        if other is None:
            return False
        if self.key != other.key or self.value != other.value:
            return False
        left_eq = self.left == other.left if self.left and other.left else self.left is other.left
        right_eq = self.right == other.right if self.right and other.right else self.right is other.right
        return left_eq and right_eq