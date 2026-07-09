"""longest_unique_substring.py

Exercise: longest_unique_substring(s)

Return the length of the longest substring without repeating characters.

Pattern (sliding window + hash map):
- Maintain a window [left..right] with unique characters.
- last_seen maps char -> last index where it was seen.
- When we see a repeated char at index right, move left to (last_seen[char] + 1)
  so the window becomes valid again.

Time:  O(n)
Space: O(min(n, alphabet_size))
"""

from __future__ import annotations


def longest_unique_substring(s: str) -> int:
    last_seen: dict[str, int] = {}

    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            # ch is repeating within the current window
            left = last_seen[ch] + 1

        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(longest_unique_substring("abcabcbb"))  # 3
    print(longest_unique_substring("bbbbb"))      # 1
    print(longest_unique_substring("pwwkew"))     # 3

