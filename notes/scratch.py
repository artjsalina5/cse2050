class ListNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self, L=None):
        self._head = None
        self._tail = None
        self._length = 0
        if L is not None:
            for data in L:
                self.addlast(data)

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
        if self._head is None:
            return None  # or raise an exception
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        if self._head is None or self._head.link is None:
            return self.removefirst()

        currentnode = self._head
        while currentnode.link.link is not None:
            currentnode = currentnode.link
        item = self._tail.data
        self._tail = currentnode
        self._tail.link = None
        self._length -= 1
        return item

    def __str__(self):
        string = "The numbers in the linked list are: "
        currentnode = self._head
        while currentnode is not None:
            string += str(currentnode.data)
            currentnode = currentnode.link
            if currentnode:  # Add arrow if not at the end
                string += "-->"
        return string

    def __iter__(self):
        currentnode = self._head
        while currentnode is not None:
            yield currentnode.data
            currentnode = currentnode.link

    def __len__(self):
        return self._length