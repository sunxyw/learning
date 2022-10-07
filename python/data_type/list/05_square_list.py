"""
Given a `get_square()` function that takes a list of numbers as an argument.
Return a list of the squares of the numbers in the list.
"""


def get_square(numbers):
    return [i ** 2 for i in numbers]


print(get_square([1, 2, 3, 4, 5]))
