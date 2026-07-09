"""word_index_search.py

Exercise: Build an in-memory inverted index.

Given a list of documents (strings):
- build inverted_index[word] = set(doc_indices) where word appears
Then implement search(query_words) returning documents containing ALL query words.

Query semantics:
- query is a list of words (or a string which we split on whitespace).
- ALL query words must be present in the document.

Time:
- Build: O(total words)
- Search: intersection of sets for each query word.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable, List, Set


def build_word_index(documents: list[str]) -> dict[str, set[int]]:
    index: dict[str, set[int]] = defaultdict(set)

    for doc_id, doc in enumerate(documents):
        words = doc.split()
        for w in words:
            index[w].add(doc_id)

    return dict(index)


def search(documents: list[str], index: dict[str, set[int]], query: str | Iterable[str]) -> list[str]:
    # Normalize query to iterable of words
    if isinstance(query, str):
        query_words = query.split()
    else:
        query_words = list(query)

    if not query_words:
        return documents.copy()

    # Start from docs containing first word
    first = query_words[0]
    if first not in index:
        return []

    common: Set[int] = set(index[first])
    for w in query_words[1:]:
        common &= index.get(w, set())
        if not common:
            return []

    return [documents[i] for i in sorted(common)]


if __name__ == "__main__":
    docs = [
        "this is a test",
        "this test is fun",
        "coding in python",
    ]
    idx = build_word_index(docs)
    print(search(docs, idx, "this test"))

