from collections import Counter


def char_frequency(s: str) -> dict[str, int]:
    """Return a frequency map of characters in the given string."""
    # Counter is the simplest correct way to count occurrences.
    return dict(Counter(s))


if __name__ == "__main__":
    result = char_frequency("hello")
    print(result)

