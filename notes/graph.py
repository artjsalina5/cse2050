from ds2.graph import AdjacencySetGraph
from ds2.priorityqueue import PriorityQueue 

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

from ds2.graph import Digraph

class Graph(Digraph):
    def addedge(self, u, v, weight = 1):
        Digraph.addedge(self, u, v, weight)
        Digraph.addedge(self, v, u, weight)

    def removeedge(self, u, v):
        Digraph.removeedge(self, u, v)
        Digraph.removeedge(self, v, u)

    def edges(self):
        E = {frozenset(e) for e in Digraph.edges(self)}
        return iter(E)

def dijkstra(G, v):
    tree = {}
    D = {v: 0}
    tovisit = PriorityQueue()
    tovisit.insert((None,v), 0)
    for a,b in tovisit:
        if b not in tree:
            tree[b] = a 
            if a is not None:
                D[b] = D[a] + G.wt(a,b)
            for n in G.nbrs(b):
                tovisit.insert((b,n), D[b] + G.wt(b,n))
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

G = Graph({1,2,3}, {(1,2,4.6), (2,3,9.2), (1,3,3.1)})
shortestpaths(G,1)
print('------------------')
G.addedge(3,2,1.1)
shortestpaths(G,1)  
