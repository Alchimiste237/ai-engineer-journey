"""subarray_sum_equals_k.py

Exercise: subarray_sum_equals_k(lst, k)

Count contiguous subarrays whose sum equals k.

O(n) prefix-sum hash map technique:
- Let prefix[i] be sum(lst[0..i]).
- A subarray (l..r) sums to k when:
    prefix[r] - prefix[l-1] = k
  -> prefix[l-1] = prefix[r] - k
- As we scan, keep counts of prefix sums seen so far.

Time:  O(n)
Space: O(n)
"""

from __future__ import annotations

from collections import defaultdict


def subarray_sum_equals_k(lst: list[int], k: int) -> int:
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1

    total = 0
    prefix = 0

    for x in lst:
        prefix += x

        # number of l where prefix[l-1] == prefix - k
        total += prefix_counts[prefix - k]
        prefix_counts[prefix] += 1

    return total


if __name__ == "__main__":
    print(subarray_sum_equals_k([1, 1, 1], 2))  # 2
    print(subarray_sum_equals_k([1, 2, 3], 3))  # 2 ([1,2], [3])

