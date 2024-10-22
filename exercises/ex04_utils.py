"""list Utility functions"""

__author__ = "730577493"


def all(a: list[int], num1: int) -> bool:
    if len(a) == 0:
        return False  # if the list is empty, num1 will not be present
    for elem in a:  # iterates through each elem in the list
        if elem != num1:
            return False  # returns earlier to interrupt if this is the case
    return True  # if all elements are equal to num1, will return True


def max(b: list[int]) -> int:
    if len(b) == 0:  # results in ValueError is list is empty
        raise ValueError("max() arg is an empty List")
    largest: int = b[0]  # stores largest value in list as code goes through it
    for elem in b:
        if elem > largest:
            largest = elem  # reassigns largest value to largest value so far in list
    return largest


def is_equal(c: list[int], d: list[int]) -> bool:
    status: bool = True  # fixes static type error so we can have return statement
    if len(c) != 0 and len(d) != 0:  # only works if both lists have elements
        for elem in c:  # goes through each elem in c
            for elem in d:  # and then goes through corresponding elem in d
                if d != c:  # to see if they are equal or not
                    status = False
                else:
                    status = True
    elif len(c) == 0 and len(d) == 0:
        status = True  # so if both lists are empty, they are considered equal
    else:
        status = (
            False  # so if one list or the other is empty, they are considered unequal
        )
    return status


def extend(e: list[int], f: list[int]) -> None:
    for elem in f:  # appends each element from f in order to the end of e
        e.append(elem)
