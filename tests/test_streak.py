import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Tests that a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -5, 0]) == 0

def test_all_positive_numbers():
    """Tests that a list with all positive numbers returns the length of the list."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Tests a simple case with a single positive streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks():
    """Tests that the function returns the length of the longest streak."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, -2, 8, 9]) == 3

def test_streak_at_beginning():
    """Tests a case where the longest streak is at the beginning of the list."""
    assert longest_positive_streak([7, 8, 9, 0, 1, 2]) == 3

def test_streak_at_end():
    """Tests a case where the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6, 7]) == 4

def test_list_with_zeros():
    """Tests that zeros correctly break a streak."""
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6]) == 3

def test_list_with_negatives():
    """Tests that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, -2, 3, 4, -5, 6, 7, 8]) == 3
