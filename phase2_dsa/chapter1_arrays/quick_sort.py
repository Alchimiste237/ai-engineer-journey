"""quick_sort.py

Exercise: Implement quick_sort(lst) and write a comparison notes.txt of:
- bubble sort
- insertion sort
- merge sort
- quick sort

This file provides:
- quick_sort implementation
- detailed comments explaining partitioning and recursion
- complexity notes

(Comparison table itself goes in notes.txt as requested.)
"""

from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


def quick_sort(lst: List[T]) -> List[T]:
    """Return a sorted copy of lst using quick sort.

    Partition strategy used here:
    - Choose the last element as the pivot.
    - Partition into: [less/equal pivot] + [pivot] + [greater pivot]

    Complexity:
    - Best / Avg: O(n log n)
    - Worst: O(n^2) (e.g., already sorted input with poor pivot choice)

    Space:
    - O(log n) average recursion depth (worst O(n) stack)

    Notes:
    - This implementation is NOT in-place; it creates new lists during recursion.
      That makes it easier to understand but uses extra memory.
    - If you want an in-place version, you would partition within the same array.
    """

    if len(lst) <= 1:
        return lst.copy()

    pivot = lst[-1]
    left: List[T] = []
    middle: List[T] = []
    right: List[T] = []

    # Distribute elements into partitions.
    # Using three-way partitioning helps with duplicates.
    for x in lst:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    # Recursively sort partitions smaller than and greater than the pivot.
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print(quick_sort(data))  # Expected: [1, 5, 7, 8, 9, 10]

