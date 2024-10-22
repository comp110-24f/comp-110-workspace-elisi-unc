"""Practice with Unit Tests"""

__author__ = "730577493"

from CQs.cq07.find_max import find_and_remove_max


def test_return_max() -> None:
    """tests that this fn will return max value"""
    input: list[int] = [2, 4, 6, 8, 10]
    assert find_and_remove_max(input) == 10


def test_remove_max() -> None:
    """tests that max values are removed from list"""
    input: list[int] = [2, 4, 6, 8, 10]
    assert find_and_remove_max(input) == [2, 4, 6, 8]


def test_edge_case() -> None:
    """tests that an empty list will return -1"""
    input = []
    assert find_and_remove_max(input) == -1
