class Tree:
    def __init__(self, L):
        iterator = iter(L)
        self.data = next(iterator)
        self.children = [Tree(c) for c in iterator]

    def _listwithlevels(self, level, trees):
        trees.append(" " * level + str(self.data))
        for child in self.children:
            child._listwithlevels(level + 1, trees)

    def __str__(self):
        trees = []
        self._listwithlevels(0, trees)
        return "\n".join(trees)

    def __eq__(self, other):
        return self.data == other.data and self.children == other.children

    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            return 1 + max(child.height() for child in self.children)

    def depth(self, level=0):
        return max([level] + [child.depth(level + 1) for child in self.children])

    def weight(self):
        return 1 + sum(child.weight() for child in self.children)

    def __contains__(self, k):
        return self.data == k or any(k in ch for ch in self.children)

    def __iter__(self):
        yield self.data
        for child in self.children:
            yield from child

    def dfs_generator(self):
        yield self.data
        for child in self.children:
            yield from child.dfs_generator()

# create a tree
T = Tree(['a', ['b', ['c', ['d']]],['e', ['f'], ['g']]])

# print the tree
print(T)

# check height of the tree
print(T.height())

# check depth
print(T.depth())

# check weight
print(T.weight())

# check if 'a' is present in the tree
print('a' in T)

# use the depth-first search generator
for node in T.dfs_generator():
    print(node)