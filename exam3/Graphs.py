class AdjacencySetGraph:
    def __init__(self, V = (), E = ()):
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for e in E: self.addedge(*e)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield (u,v)

    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def addedge(self, u, v):
        self._nbrs[u].add(v)

    def removeedge(self, u, v):
        self._nbrs[u].remove(v)

    def __contains__(self, v):
        return v in self._nbrs

    def nbrs(self, v):
        return iter(self._nbrs[v])

    def __len__(self):
      return len(self._nbrs)

    def hasedge(self, u, v):
        return v in self._nbrs[u]

    def ispath(self, V):
      """Return True if and only if the vertices V form a path."""
      return V and all(self.hasedge(V[i-1], V[i]) for i in range(1, len(V)))

    def issimplepath(self, V):
      """Return True if and only if the vertices V form a simple path."""
      return self.ispath(V) and len(V) == len(set(V))

    def iscycle(self, V):
        """Return True if and only if the vertices V form a cycle."""
        return self.ispath(V) and V[0] == V[-1]

    def issimplecycle(self, V):
        """Return True if and only if the vertices V form a simple cycle."""
        return self.iscycle(V) and self.issimplepath(V[:-1])

    def connected_recursive(self, a, b):
        if a == b: return True
        return any(self.connected_recursive(nbr, b) for nbr in self.nbrs(a))

    def connected(self, a, b):
        return self._connected(a, b, set())

    def _connected(self, a, b, visited):
        if a in visited: return False
        if a == b: return True
        visited.add(a)
        return any(self._connected(nbr, b, visited) for nbr in self.nbrs(a))

    def bfs(self, v):
        tree = {}
        tovisit = Queue()
        tovisit.enqueue((None, v))
        while tovisit:
            a, b = tovisit.dequeue()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.enqueue((b, n))
        return tree

class UndirectedGraph(AdjacencySetGraph):
    def addedge(self, u, v):
        AdjacencySetGraph.addedge(self, u, v)
        AdjacencySetGraph.addedge(self, v, u)
    def removeedge(self, u, v):
        AdjacencySetGraph.removeedge(self, u, v)
        AdjacencySetGraph.removeedge(self, v, u)
    def edges(self):
        E = {frozenset(e) for e in AdjacencySetGraph.edges(self)}
        return iter(E)

class Digraph(AdjacencySetGraph):
    def addedge(self, u, v, weight = 1):
        self._nbrs[u][v] = weight
    def removeedge(self, u, v):
        del self._nbrs[u][v]
    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = {}
    def wt(self, u, v):
        return self._nbrs[u][v]

class WeightedGraph(Digraph):
    def addedge(self, u, v, weight = 1):
        Digraph.addedge(self, u, v, weight)
        Digraph.addedge(self, v, u, weight)
    def removeedge(self, u, v):
        Digraph.removeedge(self, u, v)
        Digraph.removeedge(self, v, u)
    def edges(self):
        E = {frozenset(e) for e in Digraph.edges(self)}
        return iter(E)