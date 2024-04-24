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

def mergesort(L):
    if len(L) > 1:
        mid = len(L) // 2
        A, B = L[:mid], L[mid:]
        mergesort(A)
        mergesort(B)
        L[:] = merge(A, B)

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


# Test the function
arr = [10, 7, 8, 9, 1, 5]
print(arr)
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)