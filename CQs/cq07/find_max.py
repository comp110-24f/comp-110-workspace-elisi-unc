"""Practice with Unit Tests"""

__author__ = "730577493"


def find_and_remove_max(a: list[int]) -> int:
    max_num: int = 0
    idx: int = 0
    if len(a) == 0:
        return -1
    for elem in a:
        if elem > max_num:
            max_num = elem
    while idx < len(a):
        if max_num == a[idx]:
            a.pop(idx)
        else:
            idx += 1
    return max_num
