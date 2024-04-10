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

class Queue:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        """Adds data to the end of the queue FIFO style"""
        new_node = Node(data)  # Create a new node

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail._next = new_node  # Connect to the existing tail
            self.tail = new_node  # Update the tail reference
        self.length += 1

    def dequeue(self):
        """Removes and returns data from the beginning of the queue FIFO style"""
        if self.is_empty():
            raise Exception("Yo, your queue is empty")
        item = self.head.item  # Store the item to return
        self.head = self.head._next  # Update the head reference
        if self.head is None:  # Queue is now empty
            self.tail = None
        self.length -= 1
        return item


    def firsttwo(self):
        """Returns the first two members in the queue as a tuple, does not change the queue."""
        if self.length < 2:
            return (-1, -1)
        return (self.head.item, self.head._next.item)


    def lasttwo(self):
        """Returns the last two members in the queue as a tuple, does not change the queue."""
        if self.length < 2:
            return (-1, -1)

        current_node = self.head
        while current_node._next._next is not None:  # Traverse until the second-to-last node
            current_node = current_node._next
        return (current_node.item, self.tail.item)

    def is_empty(self):
        """"Checks if queue is empty"""
        return self.head is None

    def __len__(self):
        return self.length

