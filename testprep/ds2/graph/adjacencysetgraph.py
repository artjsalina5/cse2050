from ds2.queue import ListQueue as Queue


class AdjacencySetGraph:
    """
    Represents a graph as an adjacency set.

    This data structure allows for efficient addition of vertices and edges,
    as well as performant checks for the presence of vertices and edges.
    """

    def __init__(self, V = (), E = ()):
        """
        Initialize the graph with vertices and edges.

        Parameters:
            V (iterable): An iterable of hashable objects to add as vertices.
            E (iterable): An iterable of pairs (tuples of size two) to add as edges.
                          Each pair (u, v) represents an edge from u to v. The vertices u and v should be hashable.
        """
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for e in E: self.addedge(*e)

    def vertices(self):
        """
        Returns an iterator over all vertices in the graph.

        Returns:
            An iterator over the set of all vertices of the graph.
        """
        return iter(self._V)

    def edges(self):
        """
        Returns an iterator over all edges in the graph.

        Returns:
            An iterator over pairs, where each pair (u, v) represents an edge from u to v.
        """
        for u in self._V:
            for v in self.nbrs(u):
                yield (u,v)

    def addvertex(self, v):
        """
        Add a vertex to the graph.

        Parameters:
            v: The vertex to be added to the graph. Should be a hashable object.
        """
        self._V.add(v)
        self._nbrs[v] = set()

    def addedge(self, u, v):
        """
        Add an edge to the graph.

        Parameters:
            u: The first vertex of the edge.
            v: The second vertex of the edge.

        Returns:
            None. Modifies the graph in place by adding an edge from u to v.
        """
        self._nbrs[u].add(v)

    def removeedge(self, u, v):
        """
        Remove an edge from the graph.

        Parameters:
            u: The first vertex of the edge.
            v: The second vertex of the edge.

        Returns:
            None. Modifies the graph in place by removing the edge from u to v.
        """
        self._nbrs[u].remove(v)

    def __contains__(self, v):
        return v in self._nbrs

    def nbrs(self, v):
        """
        Return an iterator over all neighbors of the vertex v.

        Parameters:
            v: The vertex whose neighbors are to be returned.

        Returns:
            An iterator over the neighbors of v in the graph.
        """
        return iter(self._nbrs[v])

    def __len__(self):
        """
      Returns the number of vertices in the graph.

      Returns:
          int: The number of vertices in the graph.
      """
        return len(self._nbrs)

    def hasedge(self, u, v):
        """
        Checks if an edge exists from vertex u to vertex v in the graph.

        Parameters:
            u: The starting vertex of the edge.
            v: The ending vertex of the edge.

        Returns:
            bool: True if an edge from u to v exists in the graph, False otherwise.
        """
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
