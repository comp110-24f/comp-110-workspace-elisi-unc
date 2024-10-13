"""Mutating functions."""

___author___ = "730577493"


def manual_append(a: list[int], new_num: int) -> None:
    a.append(new_num)


def double(a: list[int]) -> None:
    idx: int = 0
    while idx < len(a):
        value: int = a[idx]
        a[idx] = 2 * value
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
