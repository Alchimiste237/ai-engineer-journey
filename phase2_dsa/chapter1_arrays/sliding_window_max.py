"""sliding_window_max.py

Exercise: Write a function sliding_window_max(lst, k) that returns the maximum
value in every window of size k as the window slides through the list.

Why this is useful (docstring requirement):
- Many problems become a “window over time” task.
- In time series analysis, you often want local/global features over a recent
  horizon (e.g., last k prices, last k sensor readings).
- That idea reappears in ML sequence modeling (e.g., when engineering features
  before RNNs, or reasoning about local patterns).

Example:
- lst = [1,3,-1,-3,5,3,6,7], k=3
- windows: [1,3,-1]->3, [3,-1,-3]->3, [-1,-3,5]->5, [-3,5,3]->5, [5,3,6]->6, [3,6,7]->7
- output: [3, 3, 5, 5, 6, 7]

Efficient approach (recommended):
- Use a deque of indices that keeps values in decreasing order.
- Each index enters and leaves the deque at most once => O(n).
"""

from __future__ import annotations

from collections import deque
from typing import Deque, List


def sliding_window_max(lst: List[int], k: int) -> List[int]:
    """Return the max for each contiguous subarray (window) of size k.

    Time:  O(n)
    Space: O(k) for the deque.
    """

    n = len(lst)
    if k <= 0:
        raise ValueError("k must be a positive integer")
    if n == 0:
        return []
    if k > n:
        raise ValueError("k cannot be larger than the length of lst")

    # Deque stores indices; values are kept in decreasing order by lst[index].
    dq: Deque[int] = deque()
    result: List[int] = []

    for i in range(n):
        # 1) Remove indices that are out of the current window [i-k+1, i]
        window_start = i - k + 1
        if dq and dq[0] < window_start:
            dq.popleft()

        # 2) Maintain decreasing order in deque
        # Pop smaller/equal values because they can never be the maximum
        # while the current value exists.
        while dq and lst[dq[-1]] <= lst[i]:
            dq.pop()

        dq.append(i)

        # 3) Once we have the first full window, record the max
        if i >= k - 1:
            result.append(lst[dq[0]])

    return result


if __name__ == "__main__":
    data = [1, 3, -1, -3, 5, 3, 6, 7]
    print(sliding_window_max(data, 3))  # Expected: [3, 3, 5, 5, 6, 7]

