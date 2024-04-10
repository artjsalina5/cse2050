class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    #######################################################
    # All methods below should be implemented recursively #
    #######################################################
    def add_last(self, item):
        '''Recursively adds last node to a List'''
        if self.link is not None:
            self.link.add_last(item)
        else:
            self.link = Node(item)

    def find_min(self):
        '''Recursively find the minimum by comparing itself to the link'''
        if self.link is None:
            return self.data
        else:
            return min(self.data, self.link.find_min())


#########################################################
# No changes below this point - all your work should be #
# in Node.                                              #
#########################################################
class LinkedList:
    def __init__(self, items=None):
        self._head = None
        if items is not None:
            for item in items:
                self.add_last(item)

    def add_last(self, item):
        # Edge case - first node added
        if self._head is None:
            self._head = Node(item)
        else:
            self._head.add_last(item)

    def find_min(self):
        if self._head is None:
            raise ValueError("find_min() on empty linked list")
        return self._head.find_min()
