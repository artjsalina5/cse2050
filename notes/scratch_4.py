def quicksort(L):
    _quicksort(L, 0, len(L))


def _quicksort(L, left, right):
    if right - left > 1:
        mid = partition(L, left, right)
        _quicksort(L, left, mid)
        _quicksort(L, mid + 1, right)


def partition(L, left, right):
    pivot = right - 1  # Choose the last element as pivot
    i, j = left, right - 2  # Update i and j
    while i <= j:  # Update condition to include equal case
        while L[i] < L[pivot]:
            i += 1
        while i <= j and L[j] > L[pivot]:  # Update condition to include exclude equal case
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    L[pivot], L[i] = L[i], L[pivot]  # Swap pivot with element at i
    return i  # Return i as the new pivot index


# Define the list
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Print initial unsorted list
print("Initial unsorted list:")
print(numbers)

# Call quicksort function on the list
quicksort(numbers)

# Print the sorted list
print("List after quicksort:")
print(numbers)