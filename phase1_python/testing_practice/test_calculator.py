import pytest
from calculator import add, divide, is_palindrome

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(5, 0) == 5

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_palindrome_true():
    assert is_palindrome("racecar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("nurses run") == True

def test_palindrome_false():
    assert is_palindrome("hello") == False

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True   # an empty string IS technically a palindrome

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_with_punctuation():
    # This will currently FAIL - good! It doesn't strip punctuation
    assert is_palindrome("A man, a plan, a canal: Panama") == True