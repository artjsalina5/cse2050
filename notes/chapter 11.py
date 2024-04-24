def dumbersort(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            L[i], L[i + 1] = L[i + 1], L[i]


def issorted(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True


def dumbsort(L):
    while not issorted(L):
        dumbersort(L)


L = [5, 4, 3, 2, 1]
dumbsort(L)
print(L)


def bubblesort(L):
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                keepgoing = True


def selectionsort(L):
    n = len(L)
    for i in range(n - 1):
        max_index = 0
        for index in range(n - i):
            if L[index] > L[max_index]:
                max_index = index
        L[n - i - 1], L[max_index] = L[max_index], L[n - i - 1]


def insertionsort(L):
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            j += 1


def insertionsort_front(L):
    n = len(L)
    for i in range(1, n):
        key_item = L[i]
        j = i - 1
        while j >= 0 and L[j] > key_item:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key_item

alist = [30, 100000, 54, 26, 93, 17, 77, 31, 44, 55, 20]
bubblesort(alist)
print(alist)