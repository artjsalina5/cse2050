from Entry import Entry
from Queue import Queue

...


class AdjacencySetGraph:
    ...

    def __str__(self):
        return (f"({{ {','.join([str(v) for v in self._V])} }},"
                f"{{ {','.join([str(e) for e in self.edges()])} }})")


...


class UndirectedGraph(AdjacencySetGraph):
    ...


...


class Digraph(AdjacencySetGraph):
    ...


...


class WeightedGraph(Digraph):
    ...
