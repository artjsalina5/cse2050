from ds2.queue import ListQueue as Queue
class Tree:
    def __init__(self, L):
        iterator = iter(L)
        self.data = next(iterator)
        self.children = [Tree(c) for c in iterator]
    def _listwithlevels(self, level, trees):
        trees.append("  " * level + str(self.data))
        for child in self.children:
            child._listwithlevels(level + 1, trees)

    def __eq__(self, other):
        return self.data == other.data and self.children == other.children

    def __contains__(self, k):
        return self.data == k or any(k in ch for ch in self.children)


    def __str__(self):
        trees = []
        self._listwithlevels(0, trees)

        return "\n".join(trees)

T = Tree(['a', ['b', ['c', ['d']]],['e',['f'], ['g']]])

print(str(T))
