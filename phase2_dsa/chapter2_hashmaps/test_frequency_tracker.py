from frequency_tracker import FrequencyTracker


def test_frequency_tracker_add_and_has_frequency():
    ft = FrequencyTracker()
    ft.add(1)
    ft.add(1)
    ft.add(2)

    assert ft.has_frequency(2) is True
    assert ft.has_frequency(1) is True
    assert ft.has_frequency(3) is False


def test_frequency_tracker_remove_changes_frequency():
    ft = FrequencyTracker()
    ft.add(1)
    ft.add(1)
    ft.add(2)

    ft.remove(1)  # 1 goes from freq 2 -> 1
    assert ft.has_frequency(2) is False
    assert ft.has_frequency(1) is True


def test_frequency_tracker_remove_missing_number_no_effect():
    ft = FrequencyTracker()
    ft.add(3)
    ft.remove(999)

    assert ft.has_frequency(1) is True
    assert ft.has_frequency(2) is False


def test_frequency_tracker_remove_to_zero_deletes_bucket():
    ft = FrequencyTracker()
    ft.add(5)
    ft.remove(5)  # 5 goes from freq 1 -> 0

    assert ft.has_frequency(1) is False
    assert ft.has_frequency(0) is False

