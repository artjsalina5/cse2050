class Node:
    """Class to define a node in a doubly-linked list."""

    def __init__(self, item, prev=None, _next=None):
        """Constructor of the Node, sets up the item (data), and the
        links to the previous (prev) and next (_next) nodes.
        """
        self.item = item
        self.prev = prev
        self._next = _next

    def __repr__(self):
        """Returns a representation of the Node, indicating its data and links."""
        return f"Node({self.item}, prev: {self.prev}, next: {self._next} )"


class Deque:
    """A double-ended queue (deque) implemented using a doubly-linked list.

    Provides efficient appending and popping from both ends of the queue.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, item):
        """Adds an item to the right end of the deque.

        Args:
            item: The item to be added.
        """
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def appendleft(self, item):
        """Adds an item to the left end of the deque.

        Args:
            item: The item to be added.
        """
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        """Removes and returns an item from the right end of the deque.

        Returns:
            The removed item.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        item = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None:  # Deque is now empty
            self.head = None
        else:
            self.tail.next = None
        self.length -= 1
        return item

    def popleft(self):
        """Removes and returns an item from the left end of the deque.

        Returns:
            The removed item.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("popleft from an empty deque")
        item = self.head.item
        self.head = self.head.next
        if self.head is None:  # Deque is now empty
            self.tail = None
        else:
            self.head.prev = None
        self.length -= 1
        return item

    def peek(self):
        """Returns the item at the right end of the deque without removing it.

        Returns:
            The item at the right end.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.tail.item

    def peekleft(self):
        """Returns the item at the left end of the deque without removing it.

        Returns:
            The item at the left end.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("peekleft from an empty deque")
        return self.head.item

    def is_empty(self):
        """Checks if the deque is empty."""
        return self.head is None

    def __len__(self):
        """Returns the number of items in the deque."""
        return self.length

    def __str__(self):
        """Returns a list-style representation of the data structure."""
        current_node = self.head
        result = []
        while current_node is not None:
            result.append(str(current_node.item))
            current_node = current_node._next
        return "[" + ", ".join(result) + "]"


my_deque = Deque()
my_deque.append(1)
my_deque.appendleft(0)
my_deque.append(2)

print(my_deque)  # Output: [0, 1, 2]