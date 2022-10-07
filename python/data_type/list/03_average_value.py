"""
Given a `get_average` function that takes a list of numbers as an argument.
Return the average value of the numbers in the list.
"""


def get_average(numbers):
    return sum(numbers) / len(numbers)


print(get_average([1, 2, 3, 4, 5]))
