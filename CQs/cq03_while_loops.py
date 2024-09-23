"""Practicing while loops"""

___author___ = "730577493"


def num_instances(phrase: str, search_char: str) -> int:
    """searches for instances a letter is in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
