def bubblesort(L):
    """
    Sorts a list in ascending order using Bubble Sort algorithm.

    Args:
        L (list): The list to be sorted.

    Returns:
        None. The list is sorted in-place.
    """
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                keepgoing = True
def cocktailSort(L):
    """
    Sorts a list in ascending order using Cocktail Shaker Sort algorithm.

    Args:
        L (list): The list to be sorted.

    Returns:
        None. The list is sorted in-place.
    """
    keepgoing = True
    start = 0
    end = len(L) - 1

    while keepgoing:
        keepgoing = False

        # Forward pass
        for i in range(start, end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                keepgoing = True

        # If no swaps occurred in the forward pass, the list is sorted
        if not keepgoing:
            break

        # Otherwise, prepare for the backward pass
        keepgoing = False
        end -= 1

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                keepgoing = True

        # Move the start point up, as the smallest item is in correct position
        start += 1
def test_sorting_algorithms():
    # Test case for bubble sort
    L = [4, 3, 2, 1]
    print(f"Original array for bubble sort: {L}")
    bubblesort(L)
    print(f"Sorted array using bubble sort: {L}\n")

    # Test case for cocktail sort
    L = [4, 3, 2, 1]
    print(f"Original array for cocktail sort: {L}")
    cocktailSort(L)
    print(f"Sorted array using cocktail sort: {L}")


if __name__ == "__main__":
    test_sorting_algorithms()
