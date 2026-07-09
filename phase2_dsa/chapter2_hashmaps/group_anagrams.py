"""group_anagrams.py

Exercise: group_anagrams(words)

Idea:
- Two words are anagrams if they have the same multiset of letters.
- Sort letters in each word; that sorted string becomes the dict key.

Example:
  ["eat","tea","tan","ate","nat","bat"]
  -> keys: "aet" -> [eat, tea, ate], "ant" -> [tan, nat], "abt" -> [bat]

Time:
- Sorting each word dominates: sum(len(word) * log(len(word))).
Space:
- O(n) for grouping.
"""

from __future__ import annotations

from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)

    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)

    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

