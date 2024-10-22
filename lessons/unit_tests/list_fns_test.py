"""writing a unit test practice"""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first

# unit test file must end with test.py


def test_get_first() -> None:  # fn name that tests must begin with test_
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert (
        get_first(fruits) == "apples"
    )  # we want to assert whether something is true or false


def test_remove_first_ret_value() -> None:
    """test that remove_first returns None."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) == None


def test_remove_first_behavior() -> None:
    """test that remove_first removes first element"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert fruits == ["oranges", "bananas"]


def test_get_first_edge_case() -> None:
    """Test that get_first works with empty list."""
    a: list[str] = []
    assert get_first([]) == ""
