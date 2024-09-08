"""Challenge Question 00"""

__author__ = "730577493"

"""Defining mimic function to mimic a message"""


def mimic(message: str) -> str:
    return message


def main() -> None:
    """Prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
