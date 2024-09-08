"""Practice with functions, subprograms, and calling functions"""

__author__ = "730577493"


def main_planner(guests: int) -> None:
    """entrypoint of program"""
    # used str() to convert floats and ints to str
    # included spaces where necessary for proper sentenct structure
    # issues with getting results from last three print lines,
    # ex. initially used str(tea_bags)
    # to solve, assigned arguments for all fn parameters so they refer to # of guests
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """a function to compute number of teabags based on number of guests"""
    return people * 2  # two tea bags per person


def treats(people: int) -> int:
    """computes number of treats needed based on no. of teas guests drink"""
    return int(tea_bags(people=people) * 1.5)
    # int() function used to convert float product to int.
    # issues with getting main_planner to work with keyword argument in treats
    # main planner works with tea_bags(people), but not with tea_bags(people=x)
    # ^at least when x is an integer, but tried (people=people) and that worked


def cost(tea_count: int, treat_count: int) -> float:
    """calculates cost of tea and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    """makes program runnable"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
