"""concatenation file to import for cq04"""

__author__ = "730577493"


def concat(thing1: str, thing2: str) -> str:
    return thing1 + thing2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
