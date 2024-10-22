# takes a list[str] as input and returns first element
def get_first(a: list[str]) -> str:
    return a[0]


# takes a list[str] as input and removes first element
def remove_first(a: list[str]) -> None:
    a.pop(1)


# takes a list[str] as input and returns + removes first element
def get_and_remove_first(a: list[str]) -> str:
    first: str = a[0]
    a.pop(0)
    return first  # check recording because this one is giving an error
