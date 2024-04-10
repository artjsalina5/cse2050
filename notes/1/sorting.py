def selectionSort(A): # O(N^2) for ALL cases...
    N = len(A)
    for L in range(N-1):
        smallest = L + A[L:].index(min(A[L:])) # BEWARE... this is O(N) not O(1)... we cannot find the smallest index of the minimum element of (N-L) items in O(1)
        A[smallest], A[L] = A[L], A[smallest] # Python can swap variables like this
    return A


def bubbleSort(A): # O(N^2) worst case (reverse sorted input), O(N) best case (sorted input)
    N = len(A)
    while N > 1: # at most n-1 passes
        swapped = False
        for i in range(N-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i] # Python can swap variables like this
                swapped = True
        if not swapped: # optimization
            break
        N -= 1
    return A


def selectionSort(A): # O(N^2) for ALL cases...
    N = len(A)
    for L in range(N-1):
        smallest = L + A[L:].index(min(A[L:])) # BEWARE... this is O(N) not O(1)... we cannot find the smallest index of the minimum element of (N-L) items in O(1)
        A[smallest], A[L] = A[L], A[smallest] # Python can swap variables like this
    return A


def insertionSort(A): # O(N^2) worst case (reverse sorted input), O(N) best case (sorted input)
    N = len(A)
    for i in range(1, N): # O(N)
        X = A[i] # X is the item to be inserted
        j = i-1
        while j >= 0 and A[j] > X: # can be fast or slow
            A[j+1] = A[j] # make a place for X
            j -= 1
        A[j+1] = X # index j+1 is the insertion point
    return A


def mergeSort(A): # O(N log N) worst case for ALL cases :)
    N = len(A)
    if N == 1: # base case, it is trivial to sort a single element list
        return A # just do nothing, return the list as it is

    mid = N//2 # PS: The one in VisuAlgo has right sublist 1 bigger than the left sublist when N is odd
    left = A[:mid] # from start to before mid, if N is odd, left is one less than right
    right = A[mid:] # from mid to end
    left_sorted = mergeSort(left) # recursively sort the left sublist
    assert(left_sorted == left) # left is directly modified to its sorted version, so we do not need to assign the result into variable left
    mergeSort(right) # recursively sort the right sublist

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right): # both left and right not empty
        if left[i] <= right[j]:
            A[k] = left[i] # take from left
            i += 1
        else:
            A[k] = right[j] # take from right
            j += 1
        k += 1
    while i < len(left): # has leftover from left (right is empty)
        A[k] = left[i]
        k += 1
        i += 1
    while j < len(right): # has leftover from right (left is empty)
        A[k] = right[j]
        k += 1
        j += 1

    return A


def quickSort(A, low, high): # expected O(N log N) worst case for ALL cases, the heavy time complexity analysis involving expected values are omitted
    if low < high:
        r = low + random.randrange(high-low+1) # a random index between [low..high]
        A[low], A[r] = A[r], A[low] # tada

        p = A[low] # p is the pivot
        m = low # S1 and S2 are initially empty
        for k in range(low+1, high+1): # explore the unknown region
            # case 2 (PATCHED solution to avoid TLE O(N^2) on input list with identical values)
            if A[k] < p or (A[k] == p and random.randrange(2) == 0):
                m += 1
                A[k], A[m] = A[m], A[k]
            # notice that we do nothing in case 1: A[k] > p
        A[low], A[m] = A[m], A[low] # final step, swap pivot with A[m]

        # a[low..high] ~> a[low..m-1], pivot, a[m+1..high]
        quickSort(A, low, m-1) # recursively sort left sublist
        # A[m] = pivot is already sorted after partition
        quickSort(A, m+1, high) # recursively sort right sublist

    return A



import random, time, sys

n = 200000
a = [random.randrange(1000000) for _ in range(n)]

# begin = time.time()
# print(a)
# b = bubbleSort(a)
# b = selectionSort(a)
# b = insertionSort(a)
# print(b)
# assert b == sorted(a)
# print("Elapsed time for Bubble/Selection/Insertion Sort (uncomment the line above first, be careful, this is slow): %.3fs" % (time.time()-begin))

# sys.setrecursionlimit(n) # the recursion can be very bad on non-randomized quickSort

begin = time.time()
# print(a)
b = mergeSort(a)
# print(b)
assert b == sorted(a)
print("Elapsed time for Merge Sort: %.3fs" % (time.time()-begin))

begin = time.time()
# print(a)
b = quickSort(a, 0, len(a)-1)
# print(b)
assert b == sorted(a)
print("Elapsed time for Randomized Quick Sort: %.3fs" % (time.time()-begin))