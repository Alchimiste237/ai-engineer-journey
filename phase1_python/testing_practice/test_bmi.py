# test_bmi.py
import pytest
from bmi import calculate_bmi, categorize_bmi

def test_calculate_bmi_normal():
    # 70kg, 1.75m -> ~22.86
    result = calculate_bmi(70, 1.75)
    assert round(result, 2) == 22.86

def test_calculate_bmi_zero_height_raises():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)

def test_calculate_bmi_negative_height_raises():
    with pytest.raises(ValueError):
        calculate_bmi(70, -1.75)

@pytest.mark.parametrize("bmi_value, expected_category", [
    (17, "Underweight"),
    (22, "Normal weight"),
    (27, "Overweight"),
    (35, "Obese"),
    (18.5, "Normal weight"),  # boundary check
    (25, "Overweight"),       # boundary check
])
def test_categorize_bmi(bmi_value, expected_category):
    assert categorize_bmi(bmi_value) == expected_category