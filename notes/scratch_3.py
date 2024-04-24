from ds2.tree import Tree

def printtree(T):
    iterator = iter(T)
    print(next(iterator))
    for child in iterator:
        printtree(child)
T = ['c', ['a', ['p'], ['n'], ['t']], ['o', ['n']]]
printtree(T)