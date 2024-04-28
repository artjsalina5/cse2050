from Graphs import AdjacencySetGraph, UndirectedGraph, Digraph, WeightedGraph
# The rest of the included files are not used since graphs does not call anything else... unlike the textbook it is self cotained.
class MyGraph:
    def __init__(self, GraphType=WeightedGraph):
        # Default of WeightedGraph
        if GraphType is WeightedGraph:
            self.graph = WeightedGraph()
        elif GraphType is Digraph:
            self.graph = Digraph()
        elif GraphType is UndirectedGraph:
            self.graph = UndirectedGraph()
        else:
            self.graph = AdjacencySetGraph()

    def add_vertices(self, V):
        [self.graph.addvertex(v) for v in V]

    def add_edges(self, E):
        [self.graph.addedge(*e) for e in E]

    def __str__(self):
        edges = []
        for edge in self.graph.edges():
            if len(edge) == 3:                 # third value of edge is weight
                u, v, _ = edge                 # ignore weight
            else:                               # if edge tuple does not have weight
                u, v = edge
            edges.append((u, v))              # add edge tuple without weight
        return (f"({{ {', '.join(map(str, self.graph.vertices()))} }},"
                f"{{ {', '.join(map(str, edges))} }}")

    def nbrs(self):
        for vertex in self.graph.vertices():
            neighbor_list = list(self.graph.nbrs(vertex))
            print(f'Vertex {vertex}: {", ".join(map(str, neighbor_list)) if neighbor_list else "None"}')


G = MyGraph(GraphType=UndirectedGraph)
G.add_vertices({1, 2, 3, 4})
G.add_edges({(1, 2), (2, 3), (1, 3), (3, 4)})
print(G)
G.nbrs()

G1 = MyGraph(GraphType=WeightedGraph)
G1.add_vertices({1, 2, 3, 4, 5})
G1.add_edges({(1, 2, 2), (2, 3, 3), (1, 3, 1), (3, 4, 2), (3, 5, 5)})
print(G1)
G1.nbrs()
