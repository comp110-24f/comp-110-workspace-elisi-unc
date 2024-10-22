"""defining unit tests for list utility fns"""

__author__ = "730577493"

from exercises.ex05.utils import only_evens, sub, add_at_index


# Fn 1: only_evens test 1
def test_return_only_evens() -> None:
    """Tests that this fn will return a list w only even #s from original list"""
    input: list[int] = [10, 11, 13, 14, 16]
    assert only_evens(input) == [10, 14, 16]


# Fn 1: only_evens test 2 mutation or not?
def test_mutate_only_evens() -> None:
    """Tests that this fn will not mutate the input list"""
    a: list[int] = [10, 11, 13, 14, 16]
    assert a == [10, 11, 13, 14, 16]


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
    assert input == [10, 11, 13, 14, 16]
    # NEED TO ASK HOW TO CALL FN HERE BUT ONLY ASK FOR INPUT


# Fn 2: sub test 3 edge case
def test_edge_sub() -> None:
    """Tests that if given a start index less than 0, fn will return a list beginning
    with its first original element"""
    input: list[int] = [10, 11, 13, 14, 16]
    idx1: int = -2
    idx2: int = 4
    assert sub(input, idx1, idx2) == [10, 11, 13, 14]


# Fn 3: add_at_index test 1
def test_return_add_at_index() -> None:
    """Tests that fn will return a list with given number added at proper index"""
    input: list[int] = [10, 11, 13, 14, 16]
    add_num: int = 20
    idx: int = 3
    assert add_at_index(input, add_num, idx) == [10, 11, 13, 20, 14, 16]


# Fn 3: add_at_index test 2 mutation
def test_mutate_add_at_index() -> None:
    """Tests that fn will return a modified list"""
    input: list[int] = [10, 11, 13, 14, 16]
    add_num: int = 20
    idx: int = 3
    assert input == [10, 11, 13, 20, 14, 16]  # CHECK THIS ONE TOO


# Fn 3: add_at_index test 3 edge case
def test_edge_add_at_index() -> None:
    """Tests that if an empty list is provided, add_at_index adds number at idx = 0"""
    input: list[int] = []
    add_num: int = 20
    idx: int = 3
    assert add_at_index(input, add_num, idx) == [add_num]
