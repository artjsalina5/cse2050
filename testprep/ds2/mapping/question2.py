class ListNode:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1
    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1
    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        if self._head.link is None:
            return self.removefirst()
        else:
            currentnode = self._head
            while currentnode.link.link is not None:
                currentnode = currentnode.link
            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            self._length -= 1
            return item

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.data
            node = node.link

    def __len__(self):
        return self._length

class LinkedQueue:
    def __init__(self):
        self._L = LinkedList()
    def enqueue(self, item):
        self._L.addlast(item)
    def dequeue(self):
        return self._L.removefirst()
    def peek(self):
        item = self._L.removefirst()
        self._L.addfirst(item)
        return item
    def __len__(self):
        return len(self._L)
    def isempty(self):
        return len(self) == 0

    def __str__(self):
        return ' '.join(str(item) for item in self._L)


queue = LinkedQueue()
#Test enqueue
queue.enqueue('1')
print(queue) # 1
queue.enqueue('2')
queue.enqueue('3')
print(queue) # 1 2 3

# Test dequeue
print(queue.dequeue())
print(queue) # 1

# Test peek
print(queue.peek())
print(queue) # 2 3

# Test length of the queue
print(len(queue)) # 2

# Test isempty
print(queue.isempty()) # False

# Empty the queue
queue.dequeue()
queue.dequeue()

# Test isempty
print(queue.isempty()) # True

# Empty queue output
print(queue) # Nothing
