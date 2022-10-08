"""
Reverse a list.
"""


def reverse_list(numbers):
    reversed_list = []
    for num in numbers:
        reversed_list.insert(0, num)
    return reversed_list


print(reverse_list([1, 2, 3, 4, 5]))
