"""find_common_elements.py

Exercise: find_common_elements(*lists)

Return elements common to ALL provided lists.

Approach:
- For each list, convert to a set.
- Intersect sets across all lists.

Time: O(n×m) per todo description (practically: O(total elements) with hashing)
Space: O(m)
"""

from __future__ import annotations


def find_common_elements(*lists: list[int]) -> set[int]:
    if not lists:
        return set()

    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)

    return common


if __name__ == "__main__":
    print(find_common_elements([1, 2, 3], [2, 3, 4], [0, 2, 5]))  # {2}

