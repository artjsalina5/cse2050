class EdgeSetGraph:
    def __init__(self, V = (), E = ()):
        '''Initializes a new graph with vertex set V and edge set E
        Input:
        Output:
        '''
        self._V = set()
        self._E = set()
        for v in V: self.addvertex(v)
        for u,v in E: self.addedge(u,v)

    def vertices(self):
        '''Returns an iterable collection of the vertices in the graph'''
        return iter(self._V)

    def edges(self):
        '''Returns an iterable collection of the edges in the graph'''
        return iter(self.E)

    def addvertex(self, v):
        '''Add a new vertex to the graph. The new vertex is identified with v'''
        return self._V.add(v)

    def addedge(self, u, v):
        '''Add a new edge to the graph between the verticeis with keys u and v'''
        return self._E.add((u,v))

    def removeedge(self, u, v):
        '''Remove the edge u,v from the graph between the verticeis with keys'''
        return self._E.remove((u, v))

    def __contains__(self, v):
        '''Returns True if the vertex v is in the graph and returns False otherwise'''
        return v in self._V

    def hasedge(self, u, v):
        '''Returns True if the edge (u, v) is in the graph and return False otherwise'''
        return (u, v) in self._E

    def nbrs(self,v):
        '''Returns an iterable collection of all out neighbors for the Graph ADT'''
        return (w for u,w in self._E if u == v)

    def __len__(self):
        '''Returns the number of verticies in the graph'''
        return len(self._V)


class UndirectedEdgeSetGraph(EdgeSetGraph):
    def addedge(self, u, v):
        self._E.add(frozenset({u,v}))

    def removeedge(self, u, v):
        self._E.remove(frozenset({u,v}))

    def nbrs(self, v):
        for u, w in self._E:
            if u == v:
                yield w
            elif w == v:
                yield u

# The problem here is that the neighbors method takes a very long time to compute
# We can make a Dictionary, or hashmap of the neighbors in a different ADT called the AdjacencyGraphADT

class AdjacencySetGraph:

    def __init__(self, V = (), E = ()):
        self._V = set()
        self._nbrs = {} # our secret sauce
        for v in V: self.addvertex(v)
        for e in E: self.addedge(*e) # pack argument

    def verticies(self):
        return iter(self._V)

    def edges(self): # This method is problematic.
        for u in self._V:
            for v in self.nbrs(u):
                yield (u, v)

    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set() # Update our dictionary. Our key is the vertex, the value are the neighbors

    def addedge(self, u, v):
        self._nbrs[u].add(v) # set add method

    def removeedge(self, u, v):
        self._nbrs[u].remove(v) # set remove method

    def __contains__(self, v):
        return v in self._nbrs

    def nbrs(self,v):
        return iter(self._nbrs[v])

    def __len__(self):
        return len(self._nbrs)

    def hasedge(self,u, v):
        return v in self._nbrs[u]

    def ispath(self, V):
        """Return True if and only if the vertices V form a path."""
        return V and all(self.hasedge(V[i - 1], V[i]) for i in range(1, len(V)))

    def issimplepath(self, V):
        """Return True if and only if the vertices V form a simple path."""
        return self.ispath(V) and len(V) == len(set(V))

    def iscycle(self, V):
        """Return True if and only if the vertices V form a cycle."""
        return self.ispath(V) and V[0] == V[-1]

    def issimplecycle(self, V):
        """Return True if and only if the vertices V form a simple cycle."""
        return self.iscycle(V) and self.issimplepath(V[:-1])

    def connected(self, a, b): # helper method
        return self._connected(a, b, set())

    def _connected(self, a, b, visited): # Memoization
        if a in visited: return False
        if a == b: return True
        visited.add(a)
        return any(self._connected(nbr, b, visited) for nbr in self.nbrs(a))

class UndirectedAdjacencySetGraph(AdjacencySetGraph):

    def addedge(self, u, v):
        AdjacencySetGraph.addedge(self, u, v)
        AdjacencySetGraph.addedge(self, v, u)

    def removeedge(self, u, v):
        AdjacencySetGraph.removeedge(self, u, v)
        AdjacencySetGraph.removeedge(self, v, u)

    def edges(self):
        E = {frozenset(e) for e in AdjacencySetGraph.edges(self)}
        return iter(E)








G = AdjacencySetGraph({1,2,3,4}, {(1,2),(3,1), (2,3), (3,4), (4,3)})
print("[1,2,3,1] is a path", G.ispath([1,2,3,1]))
print("[1,2,3,1] is a simple path", G.issimplepath([1,2,3,1]))
print("[1,2,3] is a simple path", G.issimplepath([1,2,3]))
print("[1,2,3] is a simple cycle:", G.issimplecycle([1,2,3]))
print("[1,2,3,1] is a simple cycle:", G.issimplecycle([1,2,3]))
print("[1,2,3,4] is a simple path:", G.issimplepath([1,2,3,4]))
print("[1,2,3,4] is a simple cycle:", G.issimplecycle([1,2,3,4]))
print("[1,2,3,4,3,1] is a cycle:", G.iscycle([1,2,3,4,3,1]))
print("[1,2,3,4,3,1] is a simple cycle:", G.issimplecycle([1,2,3,4,3,1]))

H = AdjacencySetGraph({1,2,3}, {(1,2), (2,1), (2,3)})
try:
    assert(H.connected(1,2))
    assert(H.connected(1,3))
except RecursionError:
    print('There was too much recursion!')
print('It works now!')
