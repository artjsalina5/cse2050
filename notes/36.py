def mergesort(L):
    if len(L) > 1:
        mid = len(L) // 2
        A, B = L[:mid], L[mid:]
        mergesort(A)
        mergesort(B)
        L[:] = merge(A, B)

def merge(A, B):
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i += 1
        else:
            L[i+j] = B[j]
            j += 1
    L[i+j:] = A[i:] + B[j:]

def quicksort(L):
    if len(L) > 1:
        mid = partition(L)
        quicksort(L[:mid])
        quicksort(L[mid+1:])
    return L

def partition(L):
    pivot = L[-1]
    LT = [e for e in L if e < pivot]
    ET = [e for e in L if e == pivot]
    GT = [e for e in L if e > pivot]
    return LT + ET + GT

def median(L):
    L.sort()
    return L[len(L) // 2]

from ds2.sorting.quicksort import partition

def quickselect(L, k):
    return _quickselect(L, k, 0, len(L))

def _quickselect(L, k, left, right):
    pivot = partition(L, left, right)
    if k <= pivot:
        return _quickselect(L, k, left, pivot)
    elif k == pivot + 1:
        return L[pivot]
    else:
        return _quickselect(L, k, pivot + 1, right)

