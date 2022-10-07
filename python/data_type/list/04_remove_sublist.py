"""
Given a `remove_sublist` function that takes two lists as arguments.
Remove the second list from the first list.
"""


def remove_sublist(numbers, sublist):
    for i in sublist:
        numbers.remove(i)
    return numbers


print(remove_sublist([1, 2, 3, 4, 5], [2, 3, 4]))
