class ListNode:
    def __init__(self, data, _prev = None, _next = None):
        self.data = data
        self._prev = _prev
        self._next = _next
        if _prev is not None:
            self._prev._next = self
        if _next is not None:
            self._next._prev = self

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def add_last(self, item):
        new_node = ListNode(item)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = new_node
        self._length += 1

    def __str__(self):
        node = self._head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node._next
        return ' -> '.join(nodes)

    def custom_sort(self):
        node = self._head
        while node is not None and node._next is not None:
            if node.data > node._next.data:
                node.data, node._next.data = node._next.data, node.data
                node = self._head
            else:
                node = node._next


dll = DoublyLinkedList()
for item in [5, 7, 3, 6, 8, 1]:
    dll.add_last(item)

dll.custom_sort()
print(dll)