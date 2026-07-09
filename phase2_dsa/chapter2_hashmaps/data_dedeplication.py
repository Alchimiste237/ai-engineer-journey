from collections import Counter, defaultdict


def analyze_dataset(records: list[dict]) -> dict:
    """Analyze dataset and deduplicate records by `id`.

    Returns:
        - total_records: total number of input records
        - unique_records: number of records after removing duplicates by id
        - duplicates_found: list of ids that appeared more than once
        - category_distribution: category -> count (based on unique records)
        - category_averages: category -> average of values (based on unique records)
    """

    seen_ids = set()
    duplicates = []
    unique_records = []

    for record in records:
        record_id = record["id"]
        if record_id in seen_ids:
            duplicates.append(record_id)
        else:
            seen_ids.add(record_id)
            unique_records.append(record)

    # Count by category with Counter
    category_counts = Counter(r["category"] for r in unique_records)

    # Group records by category
    by_category = defaultdict(list)
    for record in unique_records:
        by_category[record["category"]].append(record["value"])

    category_average = {
        cat: sum(vals) / len(vals) for cat, vals in by_category.items()
    }

    return {
        "total_records": len(records),
        "unique_records": len(unique_records),
        "duplicates_found": duplicates,
        "category_distribution": dict(category_counts),
        "category_averages": category_average,
    }


if __name__ == "__main__":
    records = [
        {"id": 1, "category": "A", "value": 10},
        {"id": 2, "category": "B", "value": 20},
        {"id": 1, "category": "A", "value": 10},  # duplicate
        {"id": 3, "category": "A", "value": 30},
        {"id": 4, "category": "B", "value": 40},
        {"id": 5, "category": "C", "value": 50},
    ]

    result = analyze_dataset(records)
    for key, value in result.items():
        print(f"{key}: {value}")

