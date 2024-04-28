class Node:
    def __init__(self, data, next=None):
        self.data = data
        self._next = next

class Queue:
    def __init__(self, values):
        self._head = None
        self._tail = None
        self.length = 0
        for value in values:
            self.enqueue(value)

    def enqueue(self, item):
        current_node = Node(item)
        if self._tail is None:
            self._head = current_node
            self._tail = current_node
        else:
            self._tail._next = current_node
            self._tail = current_node
        self.length += 1

    def addlast(self, item):
        if self._head is None:
            self.enqueue(item)
        else:
            currentnode = self._head
            while currentnode._next is not None:
                currentnode = currentnode._next
            currentnode._next = Node(item)
        self.length += 1

    def removefirst(self):
        item = self._head.data
        self._head = self._head._next
        self.length -= 1
        return item

    def dequeue(self, num = 1):
        if self._head is None:
            return None
        values = []
        for i in range(num):
            values.append(self._head.data)
            self._head = self._head._next
        if self._head is None:
            self._tail = None
        return values

    def __str__(self):
        queue_str = "Enqueue\u2192"
        current = self._head
        while current._next:
            queue_str += str(current.data) + "\n\t\t"
            current = current._next

        queue_str += str(current.data) + "\u2192Dequeue"

        return queue_str

    def __len__(self):
        """Returns the number of items in the deque."""
        return self.length
    def listQueue(self):
        queue_values = []
        current = self._head
        while current is not None:
            queue_values.append(current.data)
            current = current._next
        return queue_values

    def __add__(self, other):
        new_queue = Queue(self.listQueue() + other.listQueue())
        return new_queue



Q1 = Queue([1, 2, 3, 4, 5, 6])
print(Q1.dequeue(2))
print(Q1)



