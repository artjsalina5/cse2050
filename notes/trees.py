class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.key
        if self.right:
            yield from self.right

    def rotate_right(self):
        pass  # Implement a right rotation. Note: updating parent pointers might need additional logic.

    def rotate_left(self):
        pass  # Implement a left rotation.


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        # In-order generator (default).
        if self.root is not None:
            yield from self.root

    def iter_preorder(self):
        # Pre-order generator.
        def _preorder(node):
            if node is not None:
                yield node.key
                yield from _preorder(node.left)
                yield from _preorder(node.right)

        yield from _preorder(self.root)

    def iter_postorder(self):
        # Post-order generator.
        def _postorder(node):
            if node is not None:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node.key

        yield from _postorder(self.root)

    def height(self):
        def _height(node):
            if node is None:
                return -1  # By definition, the height of an empty tree is -1.
            else:
                return max(_height(node.left), _height(node.right)) + 1

        return _height(self.root)

    def depth(self, key):
        def _depth(node, depth=0):
            if node is None:
                return None
            elif node.key == key:
                return depth
            else:
                return _depth(node.left, depth + 1) or _depth(node.right, depth + 1)

        return _depth(self.root)

    def add(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._add(self.root, key)

    def _add(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._add(node.left, key)
        elif key > node.key:
            node.right = self._add(node.right, key)

        return node

    def search(self, key):
        pass  # Implement the BST search operation


class AVLTree(BinarySearchTree):
    def add(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root = self._add(self.root, key)

    def _add(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._add(node.left, key)
        elif key > node.key:
            node.right = self._add(node.right, key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balanceFactor = self._height(node.left) - self._height(node.right)

        # If the node is unbalanced
        if balanceFactor > 1:
            if key < node.left.key:  # Left Left Case
                return self._rotate_right(node)
            else:  # Left Right Case
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balanceFactor < -1:
            if key > node.right.key:  # Right Right Case
                return self._rotate_left(node)
            else:  # Right Left Case
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _height(self, node):
        if node is None:
            return -1
        return node.height

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x
