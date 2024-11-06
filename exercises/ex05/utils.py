"""implementing list utility fns"""

__author__ = "730577493"


def only_evens(a: list[int]) -> list[int]:
    b: list[int] = []  # creates new empty list to return instead of mutating a
    if len(a) == 0:
        return []
    for elem in a:  # goes through each element to see if even or not
        if elem % 2 == 0:
            b.append(elem)  # if even, elem is added to b
    return b


def sub(a_list: list[int], idx1: int, idx2: int) -> list[int]:
    b_list: list[int] = []  # start with empty list, bc not mutating a_list
    if (
        len(a_list) == 0 or idx1 >= len(a_list) or idx2 <= 0
    ):  # return empty list for any of these situations
        return []
    if idx1 < 0:  # sets index equal to zero if it is originally negative
        idx1 = 0
    if idx2 > len(
        a_list
    ):  # sets the last index equal to len of list if idx is greater/equal to
        idx2 = len(a_list)
    for idx in range(idx1, idx2):  # adds elements on those indices to another list
        b_list.append(a_list[idx])
    return b_list


def add_at_index(list_1: list[int], add_num: int, idx1: int) -> None:
    idx: int = len(list_1) - 1
    if idx1 < 0 or idx1 > len(list_1):
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # like raising Value Error in ex04 for if idx is out of range
    if len(list_1) != 0:  # if the list is not empty
        list_1.append(
            list_1[len(list_1) - 1]
        )  # appends last index of list 1 to list 1 again
        while idx > idx1:  # while idx is greater than insert index
            list_1[idx] = list_1[
                idx - 1
            ]  # reassigns elem at that idx to the one before it
            idx -= 1  # idx decreases
        list_1[idx1] = add_num  # changes elem at insert index to what we want
    if len(list_1) == 0:  # if list is empty, adds add_num to idx = 0
        list_1.append(add_num)
    return None
