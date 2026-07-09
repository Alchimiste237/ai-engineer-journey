"""find_duplicates_hashmap.py

Exercise: Write a function find_duplicates(lst) that returns only the elements that appear more than once.

Required variant:
- Implement it in O(n) using a dictionary/hashmap.

How it works:
- First pass: count occurrences of each value using a dict.
- Second pass: collect keys whose count > 1.

Complexity:
- Time:  O(n)
- Space: O(m) where m is the number of distinct values.

Comparison vs naive:
- Naive scans the list for every element -> O(n^2).
- Hashmap counts each element once -> O(n).
"""

from __future__ import annotations

from typing import Dict, List, TypeVar

T = TypeVar("T")


def find_duplicates_hashmap(lst: List[T]) -> List[T]:
    """Return unique elements that appear more than once (using hashmap counts)."""

    counts: Dict[T, int] = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1

    duplicates: List[T] = []

    # To keep a reasonable order, iterate through lst once and add a key at most once.
    # This preserves the order of first appearance among duplicates.
    added: set[T] = set()
    for x in lst:
        if counts[x] > 1 and x not in added:
            duplicates.append(x)
            added.add(x)

    return duplicates


if __name__ == "__main__":
    data = [1, 2, 3, 2, 4, 5, 3, 3]
    print(find_duplicates_hashmap(data))  # Expected: [2, 3]

