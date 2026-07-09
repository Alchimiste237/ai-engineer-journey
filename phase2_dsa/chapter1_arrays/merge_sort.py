"""merge_sort.py

Exercise: Implement merge_sort(lst) — the O(n log n) divide-and-conquer algorithm.

This file includes:
- merge_sort implementation
- a recursion-tree comment showing how [38, 27, 43, 3] is split and merged
- explanations and complexity notes
"""

from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


# Recursion tree / example (split + merge)
# Input: [38, 27, 43, 3]
#
#                         [38, 27, 43, 3]
#                     /                 \
#              [38, 27]                 [43, 3]
#             /      \                 /      \
#         [38]      [27]           [43]      [3]
#
# Merge step:
#   merge([38], [27])      -> [27, 38]
#   merge([43], [3])       -> [3, 43]
# Final merge:
#   merge([27, 38], [3, 43]) -> [3, 27, 38, 43]


def merge(left: List[T], right: List[T]) -> List[T]:
    """Merge two already-sorted lists into one sorted list.

    Time:  O(n) where n = len(left)+len(right)
    Space: O(n) for the output list
    """

    merged: List[T] = []
    i = j = 0

    # Take the smaller “front” element each time.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # One of them may still have leftovers.
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(lst: List[T]) -> List[T]:
    """Return a sorted copy of lst using merge sort.

    Approach (divide & conquer):
    1) Divide the list into two halves until we have lists of size 0 or 1.
    2) Conquer by merging sorted halves back together.

    Complexity:
    - Time:  O(n log n) for best/average/worst cases.
    - Space: O(n) extra space (for merged output and recursion).

    Notes:
    - This implementation returns a NEW list; it does not mutate the input.
    - Works for any elements that support <= comparisons.
    """

    if len(lst) <= 1:
        # A list with 0 or 1 element is already sorted.
        return lst.copy()

    mid = len(lst) // 2
    left_sorted = merge_sort(lst[:mid])
    right_sorted = merge_sort(lst[mid:])
    return merge(left_sorted, right_sorted)


if __name__ == "__main__":
    example = [38, 27, 43, 3]
    print("Original:", example)
    print("Sorted:  ", merge_sort(example))

