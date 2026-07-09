"""lru_cache.py

Exercise: Implement a LRUCache class using OrderedDict.

LRU (Least Recently Used) cache rule:
- get(key): returns value and marks key as most recently used
- put(key, value): inserts/updates; if capacity exceeded, evict least recently used

Implementation details:
- OrderedDict maintains insertion order.
- When we access a key, we move it to the end (most recent).
"""

from __future__ import annotations

from collections import OrderedDict
from typing import Optional


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int | None:
        if key not in self._cache:
            return None
        self._cache.move_to_end(key)  # mark as most recent
        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            # update value and mark most recent
            self._cache[key] = value
            self._cache.move_to_end(key)
            return

        # insert
        self._cache[key] = value

        # evict if needed
        if len(self._cache) > self.capacity:
            self._cache.popitem(last=False)  # pop least recent


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    print(c.get(1))  # 1
    c.put(3, 3)      # evicts key 2
    print(c.get(2))  # None
    c.put(4, 4)      # evicts key 1
    print(c.get(1))  # None
    print(c.get(3))  # 3
    print(c.get(4))  # 4

