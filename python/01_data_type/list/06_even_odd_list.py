"""
Given a `get_even_odd()` function.
Return a list of even and odd numbers in the list.
"""


def get_even_odd(numbers):
    return [[i for i in numbers if i % 2 == 0], [i for i in numbers if i % 2 != 0]]


print(get_even_odd([1, 2, 3, 4, 5]))
