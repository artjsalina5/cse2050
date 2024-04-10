def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L) - 1))

def bubble(L):
    n = len(L)
    for j in range(n - 1):
        swapped = False
        for i in range(n - 1 - j):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swapped = True
        if not swapped: break

def selection(L):
    n = len(L)
    for j in range(n - 1):
        max_index = 0
        for i in range(1, n-j):
            if L[i] > L[max_index]: max_index = i
        L[i], L[max_index] = L[max_index], L[i]

def insertion(L):
    n = len(L)
    for j in range(n):
        for i in range(n-1-j, n-1):
            if L[i] > L[i+1]: L[i], L[i+1] = L[i+1], L[i]
            else: break

if __name__ == '__main__':
    import random
    L = [random.randint(0,10) for i in range(1000)]
    L.append(-1)

    assert(not is_sorted(L))
    bubble(L)
    assert(is_sorted(L))

    L = [random.randint(0,10) for i in range(1000)]
    L.append(-1)

    assert(not is_sorted(L))
    selection(L)
    assert(is_sorted(L))

    L = [random.randint(0,10) for i in range(1000)]
    L.append(-1)

    assert(not is_sorted(L))
    insertion(L)
    assert(is_sorted(L))
