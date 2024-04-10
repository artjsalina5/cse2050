import time
import random
print(time.time())

def timetrials(func, L, trials = 10):
    totaltime = 0
    minimum = float('Inf')
    for i in range(trials):
        start = time.time()
        func(L)
        totaltime += time.time() - start
    print(f'Overall average time: {minimum:10.7f} List length = {len(L):d}')
def duplicates(L):
    n = len(L)
    for i in range(1, n):
        for j in range(i+1, n):
            if L[i] == L[j]:
                return True
        return False
def double(L):
    M = []
    for x in L:
        M.append(x*2)
    return M
n = 400
L = [40, 4000, 4, 4000]

from tabulate import tabulate
trials = 100
table = [['Length List', "Quadratic", "Sort", "Set"]]
for i in range(trials):
    row = [n]
    test_list = [x*2 for x in range(n)]
    row.append(timetrials(duplicates,L,trials))
    table.append(row)
print(tabulate(table, headers='firstrow'))
