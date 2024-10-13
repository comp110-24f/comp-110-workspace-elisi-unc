"""list Utility functions"""

__author__ = "730577493"


def all(a: list[int], num1: int) -> bool:
    for elem in a:  # goes through every element
        if elem == num1:  # checks if num1 is present
            return True
        else:  # result if num1 is not present
            return False


def max(b: list[int]) -> int:
    if len(b) == 0:  # results in ValueError is list is empty
        raise ValueError("max() arg is an empty List")
    largest: int = 0  # stores largest value in list as code goes through it
    # assumes that the first one will be the largest
    for elem in b:
        if elem > largest:
            largest = elem  # reassigns largest value to largest value so far in list
    return largest


def is_equal(c: list[int], d: list[int]) -> bool:
    for elem in c:  # goes through each elem in c
        for elem in d:  # and then goes through corresponding elem in d
            if d == c:  # to see if they are equal or not
                return True
            else:
                return False


def extend(e: list[int], f: list[int]) -> None:
    for elem in f:  # appends each element from f in order to the end of e
        e.append(elem)
