"""frequency_tracker.py

Exercise: Implement a FrequencyTracker supporting:
- add(num)
- remove(num)
- has_frequency(freq)

All in O(1) average, using TWO hash maps:
1) num_to_count[num] = how many times num appears
2) freq_to_nums[freq] = set of numbers with that frequency

has_frequency(freq) answers whether any number currently has that count.

Edge cases:
- Removing a number not present: do nothing
- When count becomes 0: remove num entry and update freq_to_nums.
"""

from __future__ import annotations

from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.num_to_count: dict[int, int] = {}
        self.freq_to_nums: defaultdict[int, set[int]] = defaultdict(set)

    def add(self, num: int) -> None:
        old = self.num_to_count.get(num, 0)
        new = old + 1

        if old > 0:
            self.freq_to_nums[old].discard(num)
            if not self.freq_to_nums[old]:
                del self.freq_to_nums[old]

        self.num_to_count[num] = new
        self.freq_to_nums[new].add(num)

    def remove(self, num: int) -> None:
        old = self.num_to_count.get(num, 0)
        if old == 0:
            return

        new = old - 1

        # remove num from old frequency bucket
        self.freq_to_nums[old].discard(num)
        if not self.freq_to_nums[old]:
            del self.freq_to_nums[old]

        if new == 0:
            del self.num_to_count[num]
        else:
            self.num_to_count[num] = new
            self.freq_to_nums[new].add(num)

    def has_frequency(self, freq: int) -> bool:
        if freq <= 0:
            return False
        return freq in self.freq_to_nums and len(self.freq_to_nums[freq]) > 0


if __name__ == "__main__":
    ft = FrequencyTracker()
    ft.add(1)
    ft.add(1)
    ft.add(2)
    print(ft.has_frequency(2))  # True
    ft.remove(1)
    print(ft.has_frequency(2))  # False

