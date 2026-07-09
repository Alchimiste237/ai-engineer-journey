"""two_sum_hashmap.py

Exercise: Solve two_sum cleanly using the hash map pattern.

We expose:
- two_sum(nums, target) -> tuple[int,int] (indices) or None

Pattern used:
- As we scan left-to-right, store value->index in a dict.
- For current value x, we need complement = target - x.
- If complement has been seen, we found the pair.

Time:  O(n)
Space: O(n)
"""

from __future__ import annotations

from typing import Optional, Tuple


def two_sum(nums: list[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices (i, j) such that nums[i] + nums[j] == target.

    If multiple answers exist, returns the first one found during the scan.
    If no answer exists, returns None.
    """

    seen: dict[int, int] = {}  # value -> index

    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return seen[complement], i
        seen[x] = i

    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))      # (0, 1)
    print(two_sum([3, 2, 4], 6))           # (1, 2)
    print(two_sum([-1, -2, -3, -4, -5], -8))  # (2, 4) depending on order

