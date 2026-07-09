"""find_missing_numbers.py

Exercise: find_missing_numbers(lst, n)

Given a list of integers from 1..n with some missing,
return the missing ones.

O(n) solution using a set:
- Put all numbers in a set for O(1) membership checks.
- Iterate 1..n and collect those not present.

Time:  O(n)
Space: O(n)
"""

from __future__ import annotations


def find_missing_numbers(lst: list[int], n: int) -> list[int]:
    present = set(lst)
    return [x for x in range(1, n + 1) if x not in present]


if __name__ == "__main__":
    print(find_missing_numbers([4, 3, 2, 7, 8, 2, 3, 1], 8))  # [5, 6]

