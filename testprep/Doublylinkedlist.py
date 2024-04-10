class Node:
    """Class to define a node in a linked list"""

    def __init__(self, data, prev=None, link=None):
        """
        Initializes a Node.

        Args:
            data (Any): The data to be stored in the node.
            prev (Node, optional): The previous node.
            link (Node, optional): The next node.
        """
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

    def __repr__(self):
        """
        Returns a string representation of the Node.

        Returns:
            str: A string representing the Node.
        """
        return f"Node({self.item}, {self._next} )"

class DoublyLinkedList:
    """Class to define a Doubly Linked List"""
    def __init__(self):
        """
        Initializes an empty DoublyLinkedList.
        """
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        """
        Returns the length of the DoublyLinkedList.

        Returns:
            int: The length of the DoublyLinkedList.
        """
        return self._length

    def _addbetween(self, item, before, after):
        """
        Adds a node in between two specified nodes.

        Args:
            item (Any): The data to be stored in the new node.
            before (Node): The node to place the new node after.
            after (Node): The node to place the new node before.
        """
        node = Node(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def addfirst(self, item):
        """
        Adds a node to the beginning of the DoublyLinkedList.

        Args:
            item (Any): The data to be stored in the new node.
        """
        self._addbetween(item, None, self._head)

    def addlast(self, item):
        """
        Adds a node to the end of the DoublyLinkedList.

        Args:
            item (Any): The data to be stored in the new node.
        """
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        """
        Removes a specified node from the DoublyLinkedList.

        Args:
            node (Node): The node to remove.

        Returns:
            Any: The data that was stored in the removed node.
        """
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def removefirst(self):
        """
        Removes the first node from the DoublyLinkedList.

        Returns:
            Any: The data that was stored in the removed node.
        """
        return self._remove(self._head)

    def removelast(self):
        """
        Removes the last node from the DoublyLinkedList.

        Returns:
            Any: The data that was stored in the removed node.
        """
        return self._remove(self._tail)

    def __iadd__(self, other):
        """
        Appends another DoublyLinkedList to the end of this one.

        Args:
            other (DoublyLinkedList): The DoublyLinkedList to append.

        Returns:
            DoublyLinkedList: The current DoublyLinkedList for chaining.
        """
        if other._head is not None:
            if self._head is None:
                self._head = other._head
            else:
                self._tail.link = other._head
                other._head.prev = self._tail
            self._tail = other._tail
            self._length = self._length + other._length

            # Clean up the other list.
            other.__init__()
        return self

