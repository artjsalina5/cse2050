class Node:
    """Class to define a node in a linked list"""
    def __init__(self, item, _next=None):
        """Constructor of the Node, builds the item (data) and the link to the next node _next"""
        self.item = item
        self._next = _next

    def __repr__(self):
        """Returns the Node data and what it is pointing to"""
        return f"Node({self.item}, {self._next} )"


class Stack:
    """Class to define a stack"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """Returns a simple representation of the stack."""
        current_node = self.head
        stack_str = ""
        while current_node is not None:
            stack_str += f"{current_node.item} "
            current_node = current_node._next
        return stack_str

    def push(self, item):
        """Adds new item to the stack at the top"""
        new_node = Node(item)
        new_node._next = self.head
        self.head = new_node  # Setting the new_node as head
        self.length += 1

    def pop(self):
        """Pops the last item from the stack"""
        value = self.head.item
        self.head = self.head._next
        return value

    def peek(self):
        return self.head.item

    def is_empty(self):
        return self.length == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack:", stack)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Stack after pop:", stack)