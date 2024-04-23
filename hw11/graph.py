from ds2.graph import AdjacencySetGraph
from ds2.priorityqueue import PriorityQueue


class Digraph(AdjacencySetGraph):
    def addedge(self, u, v, weight=1):
        self._nbrs[u][v] = weight

    def removeedge(self, u, v):
        del self._nbrs[u][v]

    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = {}

    def wt(self, u, v):
        return self._nbrs[u][v]


class Graph(Digraph):
    def addedge(self, u, v, weight=1):
        Digraph.addedge(self, u, v, weight)
        Digraph.addedge(self, v, u, weight)

    def removeedge(self, u, v):
        Digraph.removeedge(self, u, v)
        Digraph.removeedge(self, v, u)

    def edges(self):
        E = {frozenset(e) for e in Digraph.edges(self)}
        return iter(E)


def list_to_graph(L):
    vertices = set(range(1, len(L) + 1))
    edges = set()

    for i in range(len(L)):
        weight = L[i]
        next_index = (i + weight) % len(L)

        edges.add((i + 1, next_index + 1, weight))
        edges.add((next_index + 1, i + 1, weight))

    return vertices, edges


def dijkstra(G, v):
    tree = {}
    D = {v: 0}
    tovisit = PriorityQueue()
    tovisit.insert((None, v), 0)
    for a, b in tovisit:
        if b not in tree:
            tree[b] = a
            if a is not None:
                D[b] = D[a] + G.wt(a, b)
            for n in G.nbrs(b):
                tovisit.insert((b, n), D[b] + G.wt(b, n))
    return tree, D


def path(tree, v):
    path = []
    while v is not None:
        path.append(str(v))
        v = tree[v]
    return ' --> '.join(path)


def shortestpaths(G, v):
    tree, D = dijkstra(G, v)
    for v in G.vertices():
        print('Vertex', v, ':', path(tree, v), ", distance =", D[v])


def path_exists(G, start, end):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(G.nbrs(node))
    return False


board = [1, 5, 6, 2]
G = Graph(*list_to_graph(board))
shortestpaths(G, 4)
if path_exists(G, 1, len(board)):
    print("Path exists!")
else:
    print("Path does not exist.")

print('------------------')
G.addedge(3, 2, 1.1)
G.addedge(2, 4, 7)
G.addedge(1, 4, 2)
shortestpaths(G, 2)
