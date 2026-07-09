from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    """Return True if s1 and s2 are anagrams, else False."""
    # Counter compares character counts, which is sufficient for anagrams.
    return Counter(s1) == Counter(s2)


if __name__ == "__main__":
    result = is_anagram("hello", "olleh")
    print(result)

