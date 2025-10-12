import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positives():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negatives():
    assert longest_positive_streak([-1, -2, -3, -4, -5]) == 0

def test_mixed_numbers_single_streak():
    assert longest_positive_streak([1, 2, -3, 4, 5, 6]) == 3

def test_mixed_numbers_multiple_streaks():
    assert longest_positive_streak([1, 2, -3, 4, 5, -6, 7, 8, 9]) == 3

def test_with_zeros():
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6]) == 3

def test_single_element_positive():
    assert longest_positive_streak([5]) == 1

def test_single_element_negative():
    assert longest_positive_streak([-5]) == 0

def test_single_element_zero():
    assert longest_positive_streak([0]) == 0
