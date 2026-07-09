import pytest

from two_sum_hashmap import two_sum


def test_two_sum_normal_case():
    nums = [2, 7, 11, 15]
    assert two_sum(nums, 9) in {(0, 1), (1, 0)}


def test_two_sum_no_solution():
    nums = [1, 2, 3]
    assert two_sum(nums, 100) is None


def test_two_sum_negative_numbers():
    nums = [-1, -2, -3, -4, -5]
    # -3 + -5 = -8
    assert two_sum(nums, -8) == (2, 4) or two_sum(nums, -8) == (4, 2)

