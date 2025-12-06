#!/usr/bin/python3
"""
Module for finding a peak in a list of unsorted integers.
A peak is an element that is greater than or equal to its neighbors.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search approach.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int or None: A peak element from the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        # If the element to the right is greater, the peak must be on the right side
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        # Otherwise, the peak is at mid or on the left side
        else:
            high = mid

    # When low == high, we have found a peak
    return list_of_integers[low]
