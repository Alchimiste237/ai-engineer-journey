from collections import Counter


def most_frequent_words(paragraph: str, k: int = 3) -> list[tuple[str, int]]:
    """Return the top-k most frequent words from the paragraph.

    Note:
        This uses `split()`, so punctuation stays attached to words (e.g. "python," is a distinct token).
    """
    return Counter(paragraph.split()).most_common(k)


if __name__ == "__main__":
    paragraph = "i am learning python, i am an engineer."
    print(most_frequent_words(paragraph))

