from ds2.priorityqueue import Entry

class HeapPQ:
    """Implementation of a binary heap as a priority queue."""
    def __init__(self):
        """Initialize an empty heap."""
        self._entries = []

    def insert(self, item, priority):
        """
        Insert an item into the heap with a given priority.

        Parameters:
            item (any): the item to be inserted.
            priority (float): the priority of the item.
        """

        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries) - 1)

    def _parent(self, i):
        """
        Get parent index of a heap element located at index i.

        Parameters:
            i (int): index of the heap element.

        Returns:
            int: the index of the parent node.
        """
        return (i - 1) // 2

    def _children(self, i):
        """
        Get indices of children of heap element located at index i.

        Parameters:
            i (int): index of the heap element.

        Returns:
            range: range object of children indices.
        """
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))

    def _swap(self, a, b):
        """
        Swap heap elements at indices a and b.

        Parameters:
            a (int): index of the first element.
            b (int): index of the second element.
        """
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        """
        Restore heap property by moving the item at index i upwards.

        Parameters:
            i (int): index of the element to be moved.
        """
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] < L[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def findmin(self):
        """
        Get the highest (min) priority item from the heap.

        Returns:
            any: the item with the highest priority.
        """
        return self._entries[0].item

    def removemin(self):
        """
        Remove and return the highest priority item from the heap.

        Returns:
            any: the item removed from the heap.
        """
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item

    def _downheap(self, i):
        """
        Restore heap property by moving the item at index i downwards.

        Parameters:
            i (int): index of the element to be moved.
        """
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[i]:
                self._swap(i, child)
                self._downheap(child)

    def __len__(self):
        """
        Get the number of items in the heap.

        Returns:
            int: the number of items in the heap.
        """
        return len(self._entries)

    def _heapify(self):
        """
        Construct a valid heap from an arbitrary array.
        """
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)
