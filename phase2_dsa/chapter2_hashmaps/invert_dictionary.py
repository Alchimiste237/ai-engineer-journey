def invert_dict(d: dict):
    """Invert a dictionary mapping.

    Example:
        {"a": 1, "b": 2} -> {1: "a", 2: "b"}

    Note: If multiple keys share the same value, the last one encountered
    wins (because dictionary keys must be unique).
    """
    return {value: key for key, value in d.items()}


if __name__ == "__main__":
    d = {
        "a": 85,
        "b": 75,
        "c": 65,
        "d": 55,
        "e": 45,
    }
    print(invert_dict(d))

