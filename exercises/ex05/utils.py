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
    if idx2 >= len(
        a_list
    ):  # sets the last index equal to len of list if idx is greater/equal to
        idx2 = len(a_list) - 1
    for idx in range(idx1, idx2):  # adds elements on those indices to another list
        b_list.append(a_list[idx])
    return b_list


def add_at_index(list_1: list[int], add_num: int, idx1: int) -> None:
    if idx1 < 0 or idx1 >= len(list_1):
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # like raising Value Error in ex04 for if idx is out of range
    list_1.append(add_num)
    for idx in range(idx1, (len(list_1) - 2)):
        # for every element at every index after idx, you want to remove it and then
        # append it to the end of the list
        store: int = list_1[
            idx
        ]  # stores elements at indices that need to be moved to the right of add_num
        list_1.pop(list_1[idx])  # removes each element to be moved
        list_1.append(store)  # adds each element back in order to list
