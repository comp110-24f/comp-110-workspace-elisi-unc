"""EXO2 - Chardle - A cute step toward Wordle."""

__author__ = "730577493"


def input_word() -> str:  # Instead of the output being "None", it needs to be a string
    # so contains_char can evaluate.
    word: str = input("Enter a 5-character word: ")
    # was getting issues with constant "error: word..." message
    # but that was because I forgot spaces are characters, so I added a space after
    # the ":" following "word" above to account for the space I kept typing in
    if len(word) != 5:
        print(
            "Error: Word must contain 5 characters."
        )  # will print error message if len(word) != 5
        # print("'" + word + "'")?
        exit()
        # initially had return str(word) here as well as below, but it was messing up the exit function
        # because if I had return before exit, the exit fxn would never be reached
    else:
        # print("'" + word + "'")?
        return str(
            word
        )  # so the return value of this function can be called in later functions


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    # this will be the same format as input_word, but len() will be constricted to 1
    # instead of 5
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        # print("'" + letter + "'")
        exit()
    else:
        # print("'" + letter + "'")
        return str(letter)  # so the return value can be called upon in later functions


def contains_char(word: str, letter: str) -> None:
    index: int = 0  # index will allow us to check each letter of word
    count: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(word):  # use len function to go through each letter using index
        if word[index] == letter:
            print(str(letter) + " found at index " + str(index))
            count += (
                1  # need to increase each time a letter occurs to find total instances
            )
        index += 1  # to go from one letter to the following in while loop
    if count == 0:  # after the while loop completes,
        print("No instances of " + letter + " found in " + word)
    elif (
        count == 1
    ):  # had to include an elif fxn to account for "instance" vs. "instances"
        print(str(count) + " instance of " + letter + " found in " + word)
        # don't forget to convert count to str because it is currently an int
    else:
        print(print(str(count) + " instances of " + letter + " found in " + word))


def main() -> None:
    # simplifies process of repeatedly calling each function individually
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
