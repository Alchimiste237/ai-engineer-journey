"""find_duplicates_naive.py

Exercise: Write a function find_duplicates(lst) that returns only the elements that appear more than once.

Required variant:
- Implement it in O(n^2) (naive).

What this returns:
- A list containing each duplicated value once (not repeated counts).
- Order: the order of first time the value is detected as a duplicate (based on outer loop).

Complexity:
- Time:  O(n^2)
- Space: O(k) for k distinct duplicates (plus output list)
"""

from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")


def find_duplicates_naive(lst: List[T]) -> List[T]:
    """Naively find elements that appear more than once.

    Naive idea:
    - For each index i, count how many times lst[i] appears by scanning the whole list.
    - If it appears more than once, it's a duplicate.

    We also avoid adding the same value multiple times to the output by using
    a `seen` set.
    """

    duplicates: List[T] = []
    seen: set[T] = set()

    for i in range(len(lst)):
        value = lst[i]

        # If we already decided whether this value is duplicate, skip.
        if value in seen:
            continue

        # Count occurrences with an inner loop.
        count = 0
        for j in range(len(lst)):
            if lst[j] == value:
                count += 1
                # Small optimization: once count > 1, we can stop.
                if count > 1:
                    break

        # Mark as processed.
        seen.add(value)

        if count > 1:
            duplicates.append(value)

    return duplicates


if __name__ == "__main__":
    data = [1, 2, 3, 2, 4, 5, 3, 3]
    print(find_duplicates_naive(data))  # Expected: [2, 3]

