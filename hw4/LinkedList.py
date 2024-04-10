class Node:
    """"Class to define a node in a linked list"""
    def __init__(self, item, _next=None):
        """"Constructor of the Node, builds the item (data) and the link to the next node _next"""
        self.item = item
        self._next = _next

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
        self._head = Node(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addlast(self, item):
        """Adds a new node at the end of the linked list. Enqueue"""
        # You need to develop this method
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail._next = Node(item)
            self._tail = self._tail._next
            self._length += 1

    def removefirst(self):
        """Removes the first node from the linked list."""
        # You need to develop this method
        if self._head is None:
            return None  # or raise an exception
        item = self._head.item
        self._head = self._head._next
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        """Removes the last node from the linked list"""
        if self._head is None or self._head._next is None:
            return self.removefirst()

        currentnode = self._head
        while currentnode._next._next is not None:
            currentnode = currentnode._next
        item = self._tail.item
        self._tail = currentnode
        self._tail._next = None
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

