import random
instructions = 0

def bubblesort(L):
    global instructions
    for iteration in range(len(L) - 1):
        for i in range(len(L) - 1 - iteration):
            instructions += 1 # Increment for comparison
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]

def selectionsort(L):
    global instructions
    n = len(L)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            instructions += 1  # Increment for comparison
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

def insertionsort(L):
    global instructions
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0:
            instructions += 1  # Increment for comparison
            if L[j] > key:
                L[j + 1] = L[j]
                j -= 1
            else:
                break
        L[j + 1] = key


def merge(A, B):
    global instructions
    result = []
    i = j = 0
    while i < len(A) and j < len(B):
        instructions += 1  # Increment for comparison
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    # Extend without incrementing instructions, assuming extend isn't a set of instructions
    result.extend(A[i:])
    result.extend(B[j:])
    return result


def mergesort(L):
    if len(L) > 1:
        mid = len(L) // 2
        A, B = L[:mid], L[mid:]
        mergesort(A)
        mergesort(B)
        L[:] = merge(A, B)

def partition(L, low, high):
    global instructions
    pivot = L[high]
    i = low - 1
    for j in range(low, high):
        instructions += 1  # Increment for comparison
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[high] = L[high], L[i + 1]
    return i + 1



def quicksort(L, low, high):
    if low < high:
        pi = partition(L, low, high)
        quicksort(L, low, pi-1)
        quicksort(L, pi+1, high)


# if __name__ == "__main__":
#     # Test cases
#     test_cases = [
#         ([], []),
#         ([1], [1]),
#         ([4, 2], [2, 4]),
#         ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
#         ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
#         (random.sample(range(10), 10), sorted(random.sample(range(10), 10))),
#         ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
#         ([5, 3, 1, 2, 3, 1], [1, 1, 2, 3, 3, 5]),
#     ]
#
#     for arr, description in test_cases:
#         instructions = 0  # Reset the instruction count
#         bubblesort(arr)
#         print(f"{description} list instructions: {instructions}")


# if __name__ == "__main__":
#     # Testing mergesort
#     instructions = 0
#     arr_merge = [10, 7, 8, 9, 1, 5]
#     print("\nOriginal array for mergesort:", arr_merge)
#     mergesort(arr_merge)
#     print("Sorted array with mergesort:", arr_merge)
#     print(f"Mergesort instructions: {instructions}")
#
#     # Testing quick_sort
#     instructions = 0
#     arr_quick = [10, 7, 8, 9, 1, 5]
#     print("\nOriginal array for quicksort:", arr_quick)
#     quicksort(arr_quick, 0, len(arr_quick) - 1)
#     print("Sorted array with quicksort:", arr_quick)
#     print(f"quicksort instructions: {instructions}")
#
#     # Testing bubblesort
#     instructions = 0
#     arr_bubble = [10, 7, 8, 9, 1, 5]
#     print("\nOriginal array for bubblesort:", arr_bubble)
#     bubblesort(arr_bubble)
#     print("Sorted array with bubblesort:", arr_bubble)
#     print(f"bubblesort instructions: {instructions}")
#
#     # Testing selectionsort
#     instructions = 0
#     arr_selection = [10, 7, 8, 9, 1, 5]
#     print("\nOriginal array for selectionsort:", arr_selection)
#     selectionsort(arr_selection)
#     print("Sorted array with selectionsort:", arr_selection)
#     print(f"selectionsort instructions: {instructions}")
#
#     # Testing insertionsort
#     instructions = 0
#     arr_insertion = [10, 7, 8, 9, 1, 5]
#     print("\nOriginal array for insertionsort:", arr_insertion)
#     insertionsort(arr_insertion)
#     print("Sorted array with insertionsort:", arr_insertion)
#     print(f"insertionsort instructions: {instructions}")