def remove_duplicates_ordered(lst: list) -> list:
    """Remove duplicates while preserving the original order."""
    seen = set()
    result = []

    # Use a set for O(1) membership checks, while a list preserves order.
    for item in lst:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)

    return result


if __name__ == "__main__":
    result = remove_duplicates_ordered([21, 45, 89, 21, 5, 45, 7, 5, 7])
    print(result)

