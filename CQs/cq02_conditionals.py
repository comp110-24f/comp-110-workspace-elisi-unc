"""Practice with conditionals, local variables, and user input"""

__author__ = "730577493"


def guess_a_number() -> None:
    """function to write number guessing game"""
    secret: int = 7
    guess: int = int((input("Guess a number:")))
    x: str = str(guess)
    print("Your guess was " + x)
    if guess == secret:
        print("You got it!")
    elif guess <= secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
