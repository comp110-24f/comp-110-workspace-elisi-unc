"""Creating a wordle!"""

__author__ = "730577493"


def input_guess(secret_word_len: int) -> str:
    """Makes sure user uses correct word length"""
    guess: str = input("Enter a " + str(secret_word_len) + "-character word: ")
    while len(guess) != secret_word_len:  # no if-else needed, just a while loop
        # to ensure that the prompt "Try again" works correctly
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # reassign guess so input is prompted
    return guess  # returns and stores the word that was guessed


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Search this word for a single specified character"""
    assert len(char_guess) == 1
    idx: int = 0
    count: int = 0  # used same setup as from ex02 to get instances a char appears
    while idx < len(secret_word):
        if char_guess == secret_word[index]:
            count += 1  # to record instances a character appears in word
        idx += 1
    if count >= 1:
        return True  # then evaluates to True or False based on if
    # the letter appears based on how many times it appears.
    else:
        return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret_word: str) -> str:
    """Figures out which box should be returned at which index
    using contains_char"""
    assert len(guess) == len(secret_word)  # makes sure guess is same len as secret word
    idx: int = 0
    emoji: str = ""  # starts out blank because we don't need it to equal anything yet
    while idx < len(secret_word):
        contains_char_value: bool = contains_char(secret_word, guess[idx])
        # will use this to output yellow box if letter is present but not in right place
        # but using parameters directly from this fxn rather than from the original contains_char
        if secret_word[idx] == guess[idx]:
            emoji += GREEN_BOX  # green will show if letter from guessed word is in right place according to secret word
        elif contains_char_value is True:
            emoji += YELLOW_BOX  # yellow shows if letter from guessed word is also present in secret word
            # but not in right place
        else:
            emoji += WHITE_BOX  # white shows if letter from guessed word is not present in secret word
        idx += 1  # to go through every letter in guessed word
    return emoji


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1  # records number of turns taken
    secret_word: str = "codes"
    win_status: bool = False  # until they win, then it will be changed to True
    while (
        turn_number < 7 and win_status is False
    ):  # so player can only guess 6 times, and only as long
        # as they haven't won yet
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            win_status = (
                True  # so if player wins, game ends with congratulatory message
            )
        else:
            turn_number += 1  # increases turn # so they can't play infinitely
    if win_status is True:
        print(f"You won in {turn_number}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
# makes it possible to run Python program as a module
