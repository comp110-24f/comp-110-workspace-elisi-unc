"""defining unit tests for list utility fns"""

__author__ = "730577493"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# Fn 1: only_evens test 1
def test_return_only_evens() -> None:
    """Tests that this fn will return a list w only even #s from original list"""
    input: list[int] = [10, 11, 13, 14, 16]
    assert only_evens(input) == [10, 14, 16]


# Fn 1: only_evens test 2 mutation or not?
def test_mutate_only_evens() -> None:
    """Tests that this fn will not mutate the input list"""
    a: list[int] = [10, 11, 13, 14, 16]
    assert only_evens(a) == [10, 11, 13, 14, 16]


# Fn 1: only_evens test 3 edge case
def test_edge_only_evens() -> None:
    """Tests that this fn will return an empty list if list is empty"""
    a: list[int] = []
    assert only_evens(a) == []


# Fn 2: sub test 1
def test_return_sub() -> None:
    """Tests that this fn will return the correct subset of the original list"""
    input: list[int] = [10, 11, 13, 14, 16]
    idx1: int = 1
    idx2: int = 4
    assert sub(input, idx1, idx2) == [11, 13, 14]


# Fn 2: sub test 2 mutation
def test_mutate_sub() -> None:
    """Tests that this fn will not mutate its input list"""
    input: list[int] = [10, 11, 13, 14, 16]
    assert sub(input, 1, 4) == [10, 11, 13, 14, 16]


# Fn 2: sub test 3 edge case
def test_edge_sub() -> None:
    """tests that if given a start index less than 0, fn will return a list beginning with its first original element"""
    input: list[int] = [10, 11, 13, 14, 16]
    idx1: int = -2
    idx2: int = 4
    assert sub(input, idx1, idx2) == [10, 11, 13, 14]


# Fn 3: add_at_index test 1 Use case
def test_return_add_at_index() -> None:
    """Tests that fn will return a list with given number added at proper index"""
    input: list[int] = [10, 11, 13, 14, 16]
    assert add_at_index(input, 7, 3) == [10, 11, 13, 7, 20, 14, 16]


# Fn 3: add_at_index test 2 mutation
def test_mutate_add_at_index() -> None:
    """Tests that fn will return a modified list"""
    input: list[int] = [10, 11, 13, 14, 16]
    assert add_at_index(input, 7, 3) == [10, 11, 13, 14, 16]


# Fn 3: add_at_index test 3 edge case
def test_add_at_index_raises_indexerror() -> None:
    """Tests that if index is not within range, an IndexError is raised"""
    # your object to pass to add_at_index function
    input: list[int] = [1, 2, 3, 4, 5, 6]
    index: int = 10
    add_num: int = 7
    with pytest.raises(IndexError):
        add_at_index(input, index, add_num)
