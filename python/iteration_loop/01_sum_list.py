"""
Sum elements of a list.
"""


def sum_list(numbers):
    summ = 0
    for num in numbers:
        summ += num
    return summ


print(sum_list([1, 2, 3, 4, 5]))
