import random


def searching_n(lst, num):
    """
    Perform linear search to find the index of num in lst.

    Args:
        lst (list): The list to search in.
        num: The number to search for.

    Returns:
        int: The index of num if found, otherwise -1.
    O(1) place, O(n) runtime
    """
    for i, val in enumerate(lst):
        if val == num:
            return i
    return -1


def binary_search(lst, num):
    """
    Perform binary search to find the index of num in lst.

    Args:
        lst (list): The list to search in (assumed to be sorted).
        num: The number to search for.

    Returns:
        int: The index of num if found, otherwise -1.
    O(1) place, O(log n) runtime
    """
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1
