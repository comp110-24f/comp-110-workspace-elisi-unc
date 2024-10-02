"""basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# my_name: str = "" #literal for a string
my_numbers.append(1.5)
my_numbers.append(2.3)

print(my_numbers)

game_points: list[int] = [102, 86, 94]

# Subscription Notation/Indexing
game_points[2]

# modifying by index
game_points[1] = 72

# removing by index
game_points.pop(1)


# write a function called display
# input: list[int]
# return value: None
# Loop over the input and
# print every value
# Try calling it on game_points!
def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(game_points)
