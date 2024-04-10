# You don't need to modify this file
# It is general BST starter code
from math import floor, ceil

class BSTMap:
    """
    Represents a Binary Search Tree Map, a data structure where keys are stored in a
    sorted manner, allowing for efficient lookup, insertion, and deletion.
    """

    def __init__(self):
        """ Initializes an empty BSTMap. """
        self.root = None

    def newnode(self, key, value=None):
        """
        Creates and returns a new node of type BSTNode. This method can be
        overloaded in custom BSTMap classes to use different node types.

        Args:
            key: The key to be stored in the node.
            value (optional): The value associated with the key.

        Returns:
            A new BSTNode instance.
        """
        return BSTNode(key, value)

    def get(self, key):
        """
        Retrieves the value associated with a given key in the BSTMap.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key if found.

        Raises:
            KeyError: If the specified key is not found in the BSTMap.
        """
        if self.root is None:
            raise KeyError
        node = self.root.get(key)
        return node.value

    def put(self, key, value=None):
        """
        Adds a key-value pair to the BSTMap or updates the value if the
        key already exists. Maintains the BST property.

        Args:
            key: The key to add or update.
            value: The value to associate with the key.
        """
        if self.root is None:
            self.root = self.newnode(key, value)
        else:
            self.root = self.root.put(key, value)

    def preorder(self):
        """
        Generates key-value pairs from the BSTMap in preorder traversal order.

        Returns:
            A generator that yields key-value pairs in preorder.
        """
        for n in self.root._preorder():
            yield (n.key, n.value)

    def postorder(self):
        """
        Generates key-value pairs from the BSTMap in postorder traversal order.

        Returns:
            A generator that yields key-value pairs in postorder.
        """
        for n in self.root._postorder():
            yield (n.key, n.value)

    def __str__(self):
        """
        Returns a visual string representation of the BSTMap, with each level
        of the tree on a separate line.
        """
        return str(self.root)


class BSTNode:
    newnode = BSTMap.newnode    # use whatever BSTMap.newnode defines when creating new nodes in this class

    def __init__(self, key, value = None):
        """Create a new BSTNode"""
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def get(self, key):
        """Returns value associated with key, or raises key error if key not in mapping"""
        if key == self.key:
            return self
        if key < self.key and self.left is not None:
            return self.left.get(key)
        if key > self.key and self.right is not None:
            return self.right.get(key)
        raise KeyError

    def put(self, key, value = None):
        """Adds key:value pair to mapping (or updates value if key already in mapping)"""
        if key == self.key:
            self.value = value
        if key < self.key:
            if self.left is None: self.left = self.newnode(key,value)
            else: self.left = self.left.put(key, value)
        if key > self.key:
            if self.right is None: self.right = self.newnode(key,value)
            else: self.right = self.right.put(key, value)
        return self

    def _preorder(self):
        """Iterates through subtree rooted here in preorder"""
        yield self
        if self.left:
            for n in self.left._preorder():
                yield n
        if self.right:
            for n in self.right._preorder():
                yield n

    def _postorder(self):
        """Iterates through subtree rooted here in postorder"""
        if self.left:
            for n in self.left._postorder():
                yield n
        if self.right:
            for n in self.right._postorder():
                yield n
        yield self

    def tostring(self, L_strings, level):
        """Recursively build a list of strings representing this BST level-by-level"""
        # add a new substring the first time we reach this level
        if level == len(L_strings):
            L_strings.append([]) # Add a new sublist the first time we reach this level

            # check if we have previous aunts/uncles w/o children
            # manually add an offset on the left if we do.
            if level >= 1:
                offset = 0
                for item in L_strings[-2]:
                    offset+= len(item)
                L_strings[-1].append(' '*offset)

        # Fill in left tree
        if self.left: wa, wb = self.left.tostring(L_strings, level+1)
        else: wa=wb=0

        # write this key, including left-buffer 
        key_width = max(len(str(self.key)), 3) # use at least 3 character long keys, so we get nice looking trees
        L_strings[level].append(' '*wa + '-'*wb + f"{self.key:^{key_width}}") 

        # insert spaces to all levels below, so newly added items have the correct left-offset
        for l in range(level+1, len(L_strings)): L_strings[l].append(' '*key_width)

        # fill in the right tree
        if self.right: wc, wd = self.right.tostring(L_strings, level+1)
        else: wc=wd = 0

        # add right-buffer to this key
        L_strings[level][-1] += '-'*wc +' '*wd

        # return width of left and right trees
        return wa+wb+floor(key_width/2), wc+wd+ceil(key_width/2) 

    def __str__(self):
        L_strings = []
        self.tostring(L_strings, level = 0)
       
        # L_strings is a list of lists, e.g.:
        # [['   ---4 ---   '],                          # tree level 0
        #  ['--2 - ', '  ', '--6 - '],                  # tree level 1
        #  ['1 ', '  ', '3 ', '  ', '5 ', '  ', '7 ']]  # tree level 2


        L_joined = [''.join(level) for level in L_strings]  # join levels into 1 string each
        return '\n'.join(L_joined)                          # join all levels into 1 big string

        # Note - above could be simplified to 
        # return '\n'.join([''.join(level) for level in L_strings])
        # I left it in two steps so it's more obvious what is happening

if __name__ == '__main__':
    """Quick demo of how the string function works"""
    # Build this:
    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7
    bst1 = BSTMap()
    for i in [4, 2, 1, 3, 6, 5, 7]:
        bst1.put(i)
    print(bst1)
    # Prints this:
    #     ----- 4 ----     
    # -- 2 -      -- 6 -
    # 1     3     5     7