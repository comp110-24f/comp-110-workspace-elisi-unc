"""Practicing and implementing dictionary utility functions"""

__author__ = "730577493"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of input list"""
    inverted_dict: dict[str, str] = dict()  # begin with empty dictionary
    # to iterate over each item of the given dictionary
    for key in dict1:
        if (
            dict1[key] in inverted_dict
        ):  # if the value is found in the new dict already as a key
            raise KeyError("Duplicate key-- cannot invert")
        inverted_dict[dict1[key]] = key  # creates new element of dictionary
    return inverted_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns most-occurring color in dict"""
    occurrence: dict[str, int] = dict()
    total: int = 1
    for key in dict1:  # iterates through each key to see if it occurs more than once
        if dict1[key] in occurrence:
            occurrence[dict1[key]] += 1  # adds to occurrence if occurs more than once
        else:
            occurrence[dict1[key]] = total
    color: str = ""
    idx: int = 0
    for key in occurrence:  # then goes through newly made list
        if occurrence[key] > idx:  # if occurs mroe than once,
            idx = occurrence[key]  # idx changes to how many times the color shows up
            color = key  # color equals the color that is most common
    return color


def count(list1: list[str]) -> dict[str, int]:
    """Returns dictionary of how many times a value is in a list"""
    new_dict: dict[str, int] = dict()
    total: int = 1
    for item in list1:
        if item in new_dict:
            new_dict[item] += 1  # counts times a value shows up
        else:
            new_dict[item] = total  # if only occurs once, then 1 is stored
    return new_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Returns dict of a letter and list of words that begin with it"""
    new_dict: dict[str, list[str]] = {}
    for item in list1:
        if item[0].lower() in new_dict:
            new_dict[item[0]].append(item)  # appends item to list in dict
        else:
            new_dict[item[0].lower()] = [
                item
            ]  # new element assigned to dictionary with letter and its corresponding word
    return new_dict


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> None:
    """updates dictionary with attendance"""
    if day in dict1:  # appends student to list
        if student in dict1:
            dict1[day].append(student)
    else:
        dict1[day] = [student]  # adds day and student to dict if not alr present
