class Node:
    """"Class to define a node in a linked list"""
    def __init__(self, item, _next=None, _prev=None):
        """"Constructor of the Node, builds the item (data) and the link to the next node _next"""
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        """Returns the Node data and what it is pointing to"""
        return f"Node({self.item}, {self._next} )"

    def __iter__(self):
        """"Allows for the iteration over Nodes"""
        yield self.item
        if self._next is not None:
            yield from self._next


class LinkedList:
    """Class defining the Linked List ADT and her methods"""
    def __init__(self, items=None):
        """Initialise the LinkedList with a head, tail and length."""
        self._head = None
        self._tail = None
        self._length = 0

        if items is not None:
            for item in items:
                self.addlast(item)

    def addfirst(self, item):
        """"Adds a new node at the beginning of the linked list."""
        new_node = Node(item, self._head)
        if self._head is not None:
            self._head.prev = new_node
            self._head = new_node
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addlast(self, item):
        """Adds a new node at the end of the linked list. Enqueue"""
        new_node = Node(item, self._tail, None)
        if self._tail is not None:
            self._tail._next = new_node
        self._tail = new_node
        if self._head is None:
            self._head = new_node
        self._length += 1

    def remove_first(self):
        """Removes the first node from the linked list."""
        if self._head is None:
            return None  # or raise an exception
        item = self._head.item
        self._head = self._head._next
        if self._head is not None:
            self._head.prev = None
        else:
            self._tail = None
        self._length -= 1
        return item

    def remove_last(self):
        """Removes the last node from the linked list in O(1) time."""
        if self._tail is None:
            return None
        item = self._tail.item
        self._tail = self._tail.prev
        if self._tail is not None:
            self._tail._next = None
        else:
            self._head = None
        self._length -= 1
        return item

    def __str__(self):
        """Formats the str magic method to return human-readable representation of linked list"""
        string = 'Your linked list contains: '
        currentnode = self._head
        while currentnode is not None:
            string += str(currentnode.item)
            currentnode = currentnode._next
            if currentnode is not None:
                string += " ~and~ "
        return string

    def __len__(self):
        """Returns length of the linked list"""
        return self._length

    def __iter__(self):
        """Modifies the iter magic method to allow for iteration on linked list"""
        if self._head is not None:
            yield from self._head

    def __repr__(self):
        """Returns a more basic representation of the linked list"""
        items = []
        for item in self:
            items.append(str(item))
        return f"LinkedList({items})"

