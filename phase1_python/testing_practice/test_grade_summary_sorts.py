from grade_tracker import build_summary

def test_grade_summary_sorts_correctly():
    # Arrange: set up the data
    students = [
        {"name": "Alex", "math": 80, "science": 70, "english": 90},
        {"name": "Sam", "math": 95, "science": 95, "english": 95},
    ]

    # Act: run the function being tested
    summary = build_summary(students)

    # Assert: check the result is correct
    assert summary[0]["name"] == "Sam"   # Sam has the highest average
    assert summary[1]["name"] == "Alex"
    