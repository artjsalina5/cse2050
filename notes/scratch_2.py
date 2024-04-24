from ds2.figs import drawtree
from ds2.tree import Tree

T = Tree([1, [2, [3], [4]], [5],[6],[7,[8],[9], [10,[11]]]])
drawtree(T, 'tree_example1')